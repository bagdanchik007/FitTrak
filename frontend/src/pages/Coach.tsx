import { FormEvent, useState } from "react";
import { useNavigate } from "react-router-dom";
import { askCoach, suggestWorkout, type WorkoutSuggestion } from "../api/ai";
import { isAuthenticated } from "../lib/auth";

export function Coach() {
  const navigate = useNavigate();
  const [suggestion, setSuggestion] = useState<WorkoutSuggestion | null>(null);
  const [message, setMessage] = useState("");
  const [reply, setReply] = useState<string | null>(null);
  const [engine, setEngine] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  if (!isAuthenticated()) {
    navigate("/login");
  }

  async function onSuggest() {
    setError(null);
    setLoading(true);
    try {
      const s = await suggestWorkout({ experience: "intermediate" });
      setSuggestion(s);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Suggest failed");
    } finally {
      setLoading(false);
    }
  }

  async function onCoach(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const r = await askCoach(message);
      setReply(r.reply);
      setEngine(r.engine);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Coach failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="space-y-6 max-w-2xl">
      <div>
        <h1 className="text-2xl font-bold">AI Coach</h1>
        <p className="text-sm text-slate-400">
          Rule-based by default. Optional OpenAI when <code className="text-brand-500">OPENAI_API_KEY</code> is set.
        </p>
      </div>

      {error && <p className="text-sm text-red-400">{error}</p>}

      <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 space-y-3">
        <h2 className="font-medium">Workout suggestion</h2>
        <button
          type="button"
          disabled={loading}
          onClick={onSuggest}
          className="rounded-lg bg-brand-600 px-4 py-2.5 text-sm font-medium hover:bg-brand-700 disabled:opacity-50 touch-target"
        >
          Suggest next session
        </button>
        {suggestion && (
          <div className="text-sm space-y-2">
            <p>
              Focus: <span className="text-brand-500">{suggestion.focus}</span> · engine: {suggestion.engine}
            </p>
            <ul className="list-disc pl-5 space-y-1 text-slate-300">
              {suggestion.exercises.map((ex) => (
                <li key={ex.name}>
                  {ex.name} — {ex.sets}×{ex.reps} (rest {ex.rest_seconds}s)
                </li>
              ))}
            </ul>
            <p className="text-slate-500 text-xs">{suggestion.notes}</p>
          </div>
        )}
      </div>

      <form onSubmit={onCoach} className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 space-y-3">
        <h2 className="font-medium">Ask the coach</h2>
        <textarea
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          rows={3}
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="e.g. How should a beginner start?"
          required
        />
        <button
          type="submit"
          disabled={loading}
          className="rounded-lg border border-slate-600 px-4 py-2.5 text-sm hover:bg-slate-800 disabled:opacity-50"
        >
          Send
        </button>
        {reply && (
          <div className="text-sm text-slate-300 border-t border-slate-800 pt-3">
            <p className="text-xs text-slate-500 mb-1">engine: {engine}</p>
            <p>{reply}</p>
          </div>
        )}
      </form>
    </div>
  );
}
