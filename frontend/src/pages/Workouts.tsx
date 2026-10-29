import { FormEvent, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { createWorkout, fetchWorkouts } from "../api/workouts";
import { isAuthenticated } from "../lib/auth";
import { toInputDate } from "../lib/dates";
import { formatKg, formatMinutes } from "../lib/format";
import type { Workout } from "../types/api";


export function Workouts() {
  const navigate = useNavigate();
  const [items, setItems] = useState<Workout[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [title, setTitle] = useState("");
  const [performedAt, setPerformedAt] = useState(toInputDate());
  const [duration, setDuration] = useState("45");
  const [notes, setNotes] = useState("");
  const [saving, setSaving] = useState(false);

  function load() {
    fetchWorkouts()
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
      const mins = duration ? Number(duration) : null;
      await createWorkout({
        title: title.trim(),
        performed_at: performedAt,
        duration_minutes: mins && !Number.isNaN(mins) ? mins : null,
        notes: notes.trim() || null,
      });
      setTitle("");
      setNotes("");
      setPerformedAt(toInputDate());
      load();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Create failed");
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Workouts</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}

      <form
        onSubmit={onCreate}
        className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4"
      >
        <h2 className="text-sm font-medium text-slate-300">Log workout</h2>
        <input
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          placeholder="Title (e.g. Push Day)"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
          maxLength={150}
        />
        <div className="grid gap-3 sm:grid-cols-2">
          <label className="block text-xs text-slate-500">
            Date
            <input
              type="date"
              className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
              value={performedAt}
              onChange={(e) => setPerformedAt(e.target.value)}
              required
            />
          </label>
          <label className="block text-xs text-slate-500">
            Duration (min)
            <input
              type="number"
              min={0}
              max={600}
              className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
              value={duration}
              onChange={(e) => setDuration(e.target.value)}
            />
          </label>
        </div>
        <textarea
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          rows={2}
          placeholder="Notes (optional)"
          value={notes}
          onChange={(e) => setNotes(e.target.value)}
        />
        <button
          type="submit"
          disabled={saving}
          className="rounded-lg bg-brand-600 px-4 py-2.5 text-sm font-medium hover:bg-brand-700 disabled:opacity-50"
        >
          {saving ? "Saving…" : "Save workout"}
        </button>
      </form>

      <ul className="divide-y divide-slate-800 overflow-hidden rounded-xl border border-slate-800">
        {items.length === 0 && !error && (
          <li className="p-4 text-sm text-slate-500">No workouts yet — log your first session above.</li>
        )}
        {items.map((w) => (
          <li
            key={w.id}
            className="flex items-center justify-between bg-slate-900/40 px-4 py-3"
          >
            <div>
              <p className="font-medium">{w.title}</p>
              <p className="text-xs text-slate-500">{w.performed_at}</p>
            </div>
            <div className="text-right text-sm text-slate-400">
              {w.duration_minutes != null && <span>{formatMinutes(w.duration_minutes)}</span>}
              {w.total_volume_kg != null && (
                <span className="ml-3 text-brand-500">{formatKg(w.total_volume_kg)}</span>
              )}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
