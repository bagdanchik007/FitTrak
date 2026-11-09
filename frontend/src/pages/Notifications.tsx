import { useEffect, useState } from "react";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import { fetchNotifications, type Notification } from "../api/notifications";
import { isAuthenticated } from "../lib/auth";
import { EmptyState } from "../components/EmptyState";
import { ErrorBanner } from "../components/ErrorBanner";

export function Notifications() {
  useDocumentTitle("Alerts");
  const navigate = useNavigate();
  const [items, setItems] = useState<Notification[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    fetchNotifications()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Notifications</h1>
      {error && <ErrorBanner message={error} onDismiss={() => setError(null)} />}
      <ul className="space-y-2">
        {items.length === 0 && !error && (
          <li><EmptyState title="You are all caught up" hint="New alerts appear here." /></li>
        )}
        {items.map((n, i) => (
          <li key={`${n.kind}-${i}`} className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
            <p className="text-xs uppercase tracking-wide text-slate-500">{n.kind}</p>
            <p className="font-medium">{n.title}</p>
            <p className="text-sm text-slate-400">{n.body}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
