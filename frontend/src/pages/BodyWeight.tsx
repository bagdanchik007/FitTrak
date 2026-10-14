import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchBodyWeights, fetchWeekDelta, type BodyWeight as BW } from "../api/bodyWeights";
import { isAuthenticated } from "../lib/auth";

export function BodyWeight() {
  const navigate = useNavigate();
  const [items, setItems] = useState<BW[]>([]);
  const [delta, setDelta] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    Promise.all([fetchBodyWeights(), fetchWeekDelta()])
      .then(([list, d]) => {
        setItems(list);
        setDelta(d.delta_kg);
      })
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Body weight</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <p className="text-xs uppercase text-slate-500">7-day delta</p>
        <p className="text-2xl font-semibold text-brand-500">
          {delta == null ? "—" : `${delta > 0 ? "+" : ""}${delta} kg`}
        </p>
      </div>
      <ul className="divide-y divide-slate-800 rounded-xl border border-slate-800 overflow-hidden">
        {items.map((w) => (
          <li key={w.id} className="flex justify-between px-4 py-3 bg-slate-900/40 text-sm">
            <span className="text-slate-400">{w.recorded_at}</span>
            <span className="font-medium">{w.weight_kg} kg</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
