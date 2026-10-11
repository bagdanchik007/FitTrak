import { Link, NavLink, Outlet, useNavigate } from "react-router-dom";
import { logout } from "../api/auth";
import { isAuthenticated } from "../lib/auth";

const linkClass = ({ isActive }: { isActive: boolean }) =>
  `px-3 py-2 rounded-lg text-sm font-medium transition ${
    isActive ? "bg-brand-600 text-white" : "text-slate-300 hover:bg-slate-800"
  }`;

export function Layout() {
  const navigate = useNavigate();
  const authed = isAuthenticated();

  return (
    <div className="min-h-screen flex flex-col">
      <header className="border-b border-slate-800 bg-slate-900/80 backdrop-blur sticky top-0 z-10">
        <div className="mx-auto max-w-5xl flex items-center justify-between px-4 py-3">
          <Link to="/" className="text-lg font-semibold tracking-tight text-brand-500">
            FitTrack
          </Link>
          <nav className="flex items-center gap-1">
            {authed ? (
              <>
                <NavLink to="/dashboard" className={linkClass}>
                  Dashboard
                </NavLink>
                <NavLink to="/workouts" className={linkClass}>
                  Workouts
                </NavLink>
                <button
                  type="button"
                  className="ml-2 px-3 py-2 text-sm text-slate-400 hover:text-white"
                  onClick={() => {
                    logout();
                    navigate("/login");
                  }}
                >
                  Logout
                </button>
              </>
            ) : (
              <>
                <NavLink to="/login" className={linkClass}>
                  Login
                </NavLink>
                <NavLink to="/register" className={linkClass}>
                  Register
                </NavLink>
              </>
            )}
          </nav>
        </div>
      </header>
      <main className="flex-1 mx-auto w-full max-w-5xl px-4 py-8">
        <Outlet />
      </main>
      <footer className="border-t border-slate-800 py-4 text-center text-xs text-slate-500">
        FitTrack API client · React + TypeScript + Tailwind
      </footer>
    </div>
  );
}
