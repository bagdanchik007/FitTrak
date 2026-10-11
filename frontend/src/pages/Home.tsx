import { Link } from "react-router-dom";
import { isAuthenticated } from "../lib/auth";

export function Home() {
  const authed = isAuthenticated();
  return (
    <div className="space-y-8">
      <section className="rounded-2xl border border-slate-800 bg-gradient-to-br from-slate-900 to-slate-950 p-8">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Train smarter with <span className="text-brand-500">FitTrack</span>
        </h1>
        <p className="mt-3 max-w-xl text-slate-400">
          Domain-driven fitness backend demo UI. Log workouts, track streaks, goals and progress
          against the FastAPI API.
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          {authed ? (
            <Link
              to="/dashboard"
              className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-semibold text-white hover:bg-brand-700"
            >
              Open dashboard
            </Link>
          ) : (
            <>
              <Link
                to="/register"
                className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-semibold text-white hover:bg-brand-700"
              >
                Get started
              </Link>
              <Link
                to="/login"
                className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-200 hover:bg-slate-800"
              >
                Sign in
              </Link>
            </>
          )}
        </div>
      </section>
      <div className="grid gap-4 sm:grid-cols-3">
        {["Workouts & sets", "Streaks & recovery", "Goals & PRs"].map((t) => (
          <div key={t} className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 text-sm text-slate-300">
            {t}
          </div>
        ))}
      </div>
    </div>
  );
}
