import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchConsistency, fetchStreak } from "../api/streaks";
import { isAuthenticated } from "../lib/auth";

export function Streaks() {
  const navigate = useNavigate();
  const [streak, setStreak] = useState<Record<string, unknown> | null>(null);
  const [consistency, setConsistency] = useState<Record<string, unknown> | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    Promise.all([fetchStreak(), fetchConsistency()])
      .then(([s, c]) => {
        setStreak(s);
        setConsistency(c);
      })
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Streaks</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <div className="grid gap-4 sm:grid-cols-2">
        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
          <p className="text-xs uppercase text-slate-500">Current streak</p>
          <p className="mt-1 text-3xl font-semibold text-brand-500">
            {String(streak?.current_streak ?? "—")}
          </p>
        </div>
        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
          <p className="text-xs uppercase text-slate-500">Consistency</p>
          <p className="mt-1 text-3xl font-semibold text-brand-500">
            {consistency?.score != null ? String(consistency.score) : "—"}
          </p>
          <p className="text-xs text-slate-500">{String(consistency?.band ?? "")}</p>
        </div>
      </div>
    </div>
  );
}
