import { Link } from "react-router-dom";
import { InstallAppButton } from "../components/InstallAppButton";
import { isAuthenticated } from "../lib/auth";

export function Home() {
  const authed = isAuthenticated();
  return (
    <div className="space-y-8">
      <section className="rounded-2xl border border-slate-800 bg-gradient-to-br from-slate-900 to-slate-950 p-6 sm:p-8">
        <h1 className="text-3xl font-bold tracking-tight sm:text-4xl">
          Train smarter with <span className="text-brand-500">FitTrack</span>
        </h1>
        <p className="mt-3 max-w-xl text-slate-400">
          Same features on laptop and phone. Install the app shell or download the latest release.
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          {authed ? (
            <Link
              to="/dashboard"
              className="rounded-lg bg-slate-100 px-4 py-2 text-sm font-semibold text-slate-900 hover:bg-white"
            >
              Open dashboard
            </Link>
          ) : (
            <>
              <Link
                to="/register"
                className="rounded-lg border border-slate-600 px-4 py-2 text-sm text-slate-200 hover:bg-slate-800"
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
        <div className="mt-6 border-t border-slate-800 pt-6">
          <p className="mb-3 text-xs uppercase tracking-wide text-slate-500">Download GUI</p>
          <InstallAppButton />
        </div>
      </section>
      <div className="grid gap-4 sm:grid-cols-3">
        {["Workouts & sets", "Streaks & AI Coach", "Laptop + phone shell"].map((t) => (
          <div key={t} className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 text-sm text-slate-300">
            {t}
          </div>
        ))}
      </div>
    </div>
  );
}
