import { FormEvent, useEffect, useState } from "react"
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import { createGoal, fetchGoalsWithProgress } from "../api/goals";
import { isAuthenticated } from "../lib/auth";

export function Goals() {
  useDocumentTitle("Goals");
  const navigate = useNavigate();
  const [items, setItems] = useState<Record<string, unknown>[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [title, setTitle] = useState("");
  const [target, setTarget] = useState("");
  const [unit, setUnit] = useState("kg");
  const [saving, setSaving] = useState(false);

  function load() {
    fetchGoalsWithProgress()
      .then(setItems)
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
      const parsed = target ? Number(target) : null;
      await createGoal({
        title: title.trim(),
        target_value: parsed != null && !Number.isNaN(parsed) ? parsed : null,
        unit: unit.trim() || null,
      });
      setTitle("");
      setTarget("");
      load();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not create goal");
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Goals</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <form onSubmit={onCreate} className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <h2 className="text-sm font-medium text-slate-300">New goal</h2>
        <input
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          placeholder="Title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <div className="grid gap-3 sm:grid-cols-2">
          <input
            type="number"
            min={0}
            step="0.1"
            className="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
            placeholder="Target"
            value={target}
            onChange={(e) => setTarget(e.target.value)}
          />
          <input
            className="rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
            placeholder="Unit"
            value={unit}
            onChange={(e) => setUnit(e.target.value)}
          />
        </div>
        <button
          type="submit"
          disabled={saving}
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium hover:bg-brand-700 disabled:opacity-50"
        >
          {saving ? "Saving…" : "Add goal"}
        </button>
      </form>
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
