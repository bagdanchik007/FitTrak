import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchGoalsWithProgress } from "../api/goals";
import { isAuthenticated } from "../lib/auth";

export function Goals() {
  const navigate = useNavigate();
  const [items, setItems] = useState<Record<string, unknown>[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    fetchGoalsWithProgress()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Goals</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <ul className="space-y-3">
        {items.length === 0 && !error && (
          <li className="text-sm text-slate-500">No goals yet.</li>
        )}
        {items.map((g) => (
          <li
            key={String(g.id)}
            className="rounded-xl border border-slate-800 bg-slate-900/50 p-4"
          >
            <div className="flex items-start justify-between gap-3">
              <div>
                <p className="font-medium">{String(g.title)}</p>
                <p className="text-xs text-slate-500">
                  {String(g.current_value ?? 0)} / {String(g.target_value ?? "—")}{" "}
                  {String(g.unit ?? "")}
                </p>
              </div>
              <span className="rounded-full bg-slate-800 px-2 py-0.5 text-xs text-brand-500">
                {String(g.status ?? (g.is_completed ? "completed" : "open"))}
              </span>
            </div>
            {typeof g.percent_complete === "number" && (
              <div className="mt-3 h-2 overflow-hidden rounded-full bg-slate-800">
                <div
                  className="h-full bg-brand-600"
                  style={{ width: `${Math.min(100, g.percent_complete)}%` }}
                />
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
}
