import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchActivity, type ActivityItem } from "../api/activity";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { isAuthenticated } from "../lib/auth";

export function Activity() {
  useDocumentTitle("Activity");
  const navigate = useNavigate();
  const [items, setItems] = useState<ActivityItem[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    fetchActivity()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Activity</h1>
      <p className="text-sm text-slate-400">Recent workouts and weigh-ins.</p>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <ul className="space-y-2">
        {items.length === 0 && !error && (
          <li className="text-sm text-slate-500">Nothing logged yet.</li>
        )}
        {items.map((item, i) => (
          <li
            key={`${item.type}-${item.occurred_on}-${i}`}
            className="rounded-xl border border-slate-800 bg-slate-900/50 px-4 py-3"
          >
            <p className="text-xs uppercase tracking-wide text-slate-500">
              {item.meta?.label || item.type}
            </p>
            <p className="font-medium">{item.title}</p>
            <p className="text-xs text-slate-500">{item.occurred_on}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
