import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchJournal, type JournalEntry } from "../api/journal";
import { isAuthenticated } from "../lib/auth";

export function Journal() {
  const navigate = useNavigate();
  const [items, setItems] = useState<JournalEntry[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    fetchJournal()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Journal</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <ul className="space-y-2">
        {items.length === 0 && !error && (
          <li className="text-sm text-slate-500">No journal entries yet.</li>
        )}
        {items.map((e) => (
          <li key={e.id} className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
            <p className="text-xs text-slate-500">{e.entry_date || e.created_at}</p>
            {e.mood && <p className="text-brand-500 text-sm">{e.mood}</p>}
            <p className="text-sm text-slate-300">{e.notes || "—"}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
