import { FormEvent, useEffect, useState } from "react";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import { calcCalories, calcSteps, listCalcActivities } from "../api/healthCalc";
import { isAuthenticated } from "../lib/auth";
import { ErrorBanner } from "../components/ErrorBanner";
import { StatCard } from "../components/StatCard";

export function Calculators() {
  useDocumentTitle("Calculators");
  const navigate = useNavigate();
  const [error, setError] = useState<string | null>(null);
  const [activities, setActivities] = useState<string[]>(["general", "strength", "walking"]);
  const [weight, setWeight] = useState(75);
  const [duration, setDuration] = useState(45);
  const [activity, setActivity] = useState("strength");
  const [kcal, setKcal] = useState<number | null>(null);
  const [steps, setSteps] = useState(8000);
  const [height, setHeight] = useState(175);
  const [stepResult, setStepResult] = useState<{
    steps: number;
    distance_km: number;
    kcal_estimate: number;
  } | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    listCalcActivities()
      .then((r) => setActivities(r.activities?.length ? r.activities : activities))
      .catch(() => undefined);
  }, [navigate]);

  async function onCalories(e: FormEvent) {
    e.preventDefault();
    setError(null);
    try {
      const r = await calcCalories(weight, duration, activity);
      setKcal(r.kcal);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Calorie calc failed");
    }
  }

  async function onSteps(e: FormEvent) {
    e.preventDefault();
    setError(null);
    try {
      const r = await calcSteps({ steps, height_cm: height, weight_kg: weight });
      setStepResult(r);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Steps calc failed");
    }
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Calorie & step calculators</h1>
      <p className="text-sm text-slate-400">
        Rule-based estimates for portfolio demos — not medical advice.
      </p>
      {error && <ErrorBanner message={error} onDismiss={() => setError(null)} />}

      <form onSubmit={onCalories} className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <h2 className="text-sm font-medium text-slate-300">Session calories</h2>
        <label className="block text-sm text-slate-400">
          Body weight (kg)
          <input
            type="number"
            min={30}
            max={250}
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100"
            value={weight}
            onChange={(e) => setWeight(Number(e.target.value))}
          />
        </label>
        <label className="block text-sm text-slate-400">
          Duration (minutes)
          <input
            type="number"
            min={1}
            max={600}
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100"
            value={duration}
            onChange={(e) => setDuration(Number(e.target.value))}
          />
        </label>
        <label className="block text-sm text-slate-400">
          Activity
          <select
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100"
            value={activity}
            onChange={(e) => setActivity(e.target.value)}
          >
            {activities.map((a) => (
              <option key={a} value={a}>
                {a}
              </option>
            ))}
          </select>
        </label>
        <button
          type="submit"
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium hover:bg-brand-700"
        >
          Estimate kcal
        </button>
        {kcal != null && (
          <div className="pt-2">
            <StatCard label="Estimated burn" value={`${kcal} kcal`} hint={activity} />
          </div>
        )}
      </form>

      <form onSubmit={onSteps} className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <h2 className="text-sm font-medium text-slate-300">Steps</h2>
        <label className="block text-sm text-slate-400">
          Steps
          <input
            type="number"
            min={0}
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100"
            value={steps}
            onChange={(e) => setSteps(Number(e.target.value))}
          />
        </label>
        <label className="block text-sm text-slate-400">
          Height (cm)
          <input
            type="number"
            min={100}
            max={230}
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-slate-100"
            value={height}
            onChange={(e) => setHeight(Number(e.target.value))}
          />
        </label>
        <button
          type="submit"
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium hover:bg-brand-700"
        >
          Estimate distance & kcal
        </button>
        {stepResult && (
          <div className="grid gap-3 sm:grid-cols-3 pt-2">
            <StatCard label="Steps" value={stepResult.steps} />
            <StatCard label="Distance" value={`${stepResult.distance_km} km`} />
            <StatCard label="kcal (approx)" value={stepResult.kcal_estimate} />
          </div>
        )}
      </form>
    </div>
  );
}
