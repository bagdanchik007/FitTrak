import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchWorkouts } from "../api/dashboard";
import { isAuthenticated } from "../lib/auth";
import type { Workout } from "../types/api";

export function Workouts() {
  const navigate = useNavigate();
  const [items, setItems] = useState<Workout[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    fetchWorkouts()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Workouts</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <ul className="divide-y divide-slate-800 rounded-xl border border-slate-800 overflow-hidden">
        {items.length === 0 && !error && (
          <li className="p-4 text-sm text-slate-500">No workouts yet. Create some via the API.</li>
        )}
        {items.map((w) => (
          <li key={w.id} className="flex items-center justify-between bg-slate-900/40 px-4 py-3">
            <div>
              <p className="font-medium">{w.title}</p>
              <p className="text-xs text-slate-500">{w.performed_at}</p>
            </div>
            <div className="text-right text-sm text-slate-400">
              {w.duration_minutes != null && <span>{w.duration_minutes} min</span>}
              {w.total_volume_kg != null && (
                <span className="ml-3 text-brand-500">{w.total_volume_kg} kg</span>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
