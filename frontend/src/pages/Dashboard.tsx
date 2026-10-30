import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { me } from "../api/auth";
import { fetchDashboard, fetchStreak, fetchWorkouts } from "../api/dashboard";
import { fetchRecoveryHint, type RecoveryHint } from "../api/meta";
import { isAuthenticated } from "../lib/auth";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import type { Dashboard as Dash, UserMe, Workout } from "../types/api";

function VolumeChart({ workouts }: { workouts: Workout[] }) {
  const points = workouts
    .slice(0, 7)
    .reverse()
    .map((w) => Number(w.total_volume_kg ?? 0));
  const max = Math.max(...points, 1);
  const w = 320;
  const h = 100;
  const barW = points.length ? w / points.length - 6 : 0;

  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
      <p className="text-xs uppercase tracking-wide text-slate-500 mb-3">
        Recent volume (kg)
      </p>
      {points.length === 0 ? (
        <p className="text-sm text-slate-500">No workout volume yet.</p>
      ) : (
        <svg viewBox={`0 0 ${w} ${h}`} className="w-full max-w-md h-28" role="img" aria-label="Volume chart">
          {points.map((v, i) => {
            const barH = (v / max) * (h - 10);
            const x = i * (barW + 6) + 4;
            const y = h - barH;
            return (
              <rect
                key={i}
                x={x}
                y={y}
                width={barW}
                height={barH}
                rx={3}
                className="fill-sky-500"
              />
            );
          })}
        </svg>
      )}
    </div>
  );
}

export function Dashboard() {
  const navigate = useNavigate();
  const [user, setUser] = useState<UserMe | null>(null);
  const [dash, setDash] = useState<Dash | null>(null);
  const [streak, setStreak] = useState<Record<string, unknown> | null>(null);
  const [workouts, setWorkouts] = useState<Workout[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [recovery, setRecovery] = useState<RecoveryHint | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    Promise.all([me(), fetchDashboard(), fetchStreak(), fetchWorkouts()])
      .then(async ([u, d, s, w]) => {
        const list = Array.isArray(w) ? w : [];
        setUser(u);
        setDash(d);
        setStreak(s);
        setWorkouts(list);
        const cutoff = Date.now() - 7 * 24 * 60 * 60 * 1000;
        const recent = list.filter((item) => {
          const t = Date.parse(String(item.performed_at));
          return !Number.isNaN(t) && t >= cutoff;
        }).length;
        try {
          setRecovery(await fetchRecoveryHint(recent));
        } catch {
          setRecovery(null);
        }
      })
      .catch((e) => setError(e instanceof Error ? e.message : "Failed to load"));
  }, [navigate]);

  if (error) {
    return <p className="text-red-400 text-sm">{error}</p>;
  }
  if (!user) {
    return <p className="text-slate-400 text-sm">Loading dashboard…</p>;
  }

  const cards = [
    { label: "Workouts", value: dash?.total_workouts ?? "—" },
    { label: "Volume (kg)", value: dash?.total_volume_kg ?? "—" },
    { label: "Active goals", value: dash?.active_goals ?? "—" },
    { label: "Streak", value: streak?.current_streak ?? dash?.current_streak ?? "—" },
  ];

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">Dashboard</h1>
        <p className="text-slate-400 text-sm">Welcome back, {user.full_name || user.email}</p>
      </div>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
        {cards.map((c) => (
          <div key={c.label} className="rounded-xl border border-slate-800 bg-slate-900/60 p-4">
            <p className="text-xs uppercase tracking-wide text-slate-500">{c.label}</p>
            <p className="mt-1 text-2xl font-semibold text-brand-500">{String(c.value)}</p>
          </div>
        ))}
      </div>
      {recovery && (
        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 text-sm">
          <p className="text-xs uppercase tracking-wide text-slate-500">Recovery</p>
          <p className="mt-1 font-medium">
            {recovery.rest_recommended
              ? "A rest day looks sensible this week."
              : "You have room for another session."}
          </p>
          <p className="text-xs text-slate-500">{recovery.reason.replace(/_/g, " ")}</p>
        </div>
      )}
      <VolumeChart workouts={workouts} />
      <Link to="/activity" className="mr-4 inline-block text-sm text-brand-500 hover:underline">
        Open activity →
      </Link>
      <Link to="/workouts" className="inline-block text-sm text-brand-500 hover:underline">
        View recent workouts →
      </Link>
    </div>
  );
}
