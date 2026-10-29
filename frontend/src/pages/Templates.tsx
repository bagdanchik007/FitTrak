import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchTemplates, type Template } from "../api/templates";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { isAuthenticated } from "../lib/auth";

export function Templates() {
  useDocumentTitle("Templates");
  const navigate = useNavigate();
  const [items, setItems] = useState<Template[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    fetchTemplates()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Templates</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <ul className="space-y-2">
        {items.length === 0 && !error && (
          <li className="text-sm text-slate-500">No templates yet.</li>
        )}
        {items.map((t) => (
          <li key={t.id} className="rounded-xl border border-slate-800 bg-slate-900/50 p-3 text-sm">
            {String(t.name || t.title || t.id)}
          </li>
        ))}
      </ul>
    </div>
  );
}
