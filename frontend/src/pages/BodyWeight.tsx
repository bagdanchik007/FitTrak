import { FormEvent, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  createBodyWeight,
  fetchBodyWeights,
  fetchWeekDelta,
  type BodyWeight as BW,
} from "../api/bodyWeights";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { toInputDate } from "../lib/dates";
import { isAuthenticated } from "../lib/auth";

export function BodyWeight() {
  useDocumentTitle("Weight");
  const navigate = useNavigate();
  const [items, setItems] = useState<BW[]>([]);
  const [delta, setDelta] = useState<number | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [kg, setKg] = useState("");
  const [day, setDay] = useState(toInputDate());
  const [saving, setSaving] = useState(false);

  function load() {
    Promise.all([fetchBodyWeights(), fetchWeekDelta()])
      .then(([list, d]) => {
        setItems(list);
        setDelta(d.delta_kg);
      })
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    load();
  }, [navigate]);

  async function onCreate(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setSaving(true);
    try {
      await createBodyWeight({ weight_kg: Number(kg), recorded_at: day });
      setKg("");
      load();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not save weight");
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Body weight</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <form onSubmit={onCreate} className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <h2 className="text-sm font-medium text-slate-300">Log weigh-in</h2>
        <div className="grid gap-3 sm:grid-cols-2">
          <input
            type="number"
            required
            min={1}
            max={500}
            step="0.1"
            className="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
            placeholder="kg"
            value={kg}
            onChange={(e) => setKg(e.target.value)}
          />
          <input
            type="date"
            required
            className="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
            value={day}
            onChange={(e) => setDay(e.target.value)}
          />
        </div>
        <button
          type="submit"
          disabled={saving}
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium hover:bg-brand-700 disabled:opacity-50"
        >
          {saving ? "Saving…" : "Save weigh-in"}
        </button>
      </form>
      <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <p className="text-xs uppercase text-slate-500">7-day delta</p>
        <p className="text-2xl font-semibold text-brand-500">
          {delta == null ? "—" : `${delta > 0 ? "+" : ""}${delta} kg`}
        </p>
      </div>
      <ul className="divide-y divide-slate-800 overflow-hidden rounded-xl border border-slate-800">
        {items.length === 0 && !error && (
          <li className="px-4 py-3 text-sm text-slate-500">No weigh-ins yet.</li>
        )}
        {items.map((w) => (
          <li key={w.id} className="flex justify-between bg-slate-900/40 px-4 py-3 text-sm">
            <span className="text-slate-400">{w.recorded_at}</span>
            <span className="font-medium">{w.weight_kg} kg</span>
          </li>
        ))}
      </ul>
    </div>
  );
}
