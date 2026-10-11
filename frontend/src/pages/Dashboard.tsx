import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { me } from "../api/auth";
import { fetchDashboard, fetchStreak } from "../api/dashboard";
import { isAuthenticated } from "../lib/auth";
import type { Dashboard as Dash, UserMe } from "../types/api";

export function Dashboard() {
  const navigate = useNavigate();
  const [user, setUser] = useState<UserMe | null>(null);
  const [dash, setDash] = useState<Dash | null>(null);
  const [streak, setStreak] = useState<Record<string, unknown> | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    Promise.all([me(), fetchDashboard(), fetchStreak()])
      .then(([u, d, s]) => {
        setUser(u);
        setDash(d);
        setStreak(s);
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
      <Link to="/workouts" className="inline-block text-sm text-brand-500 hover:underline">
        View recent workouts →
      </Link>
    </div>
  );
}
