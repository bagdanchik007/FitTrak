import { useEffect, useState } from "react";
import { Link, NavLink, Outlet, useLocation, useNavigate } from "react-router-dom";
import { logout } from "../api/auth";
import { isAuthenticated } from "../lib/auth";

const RELEASES_URL =
  import.meta.env.VITE_APP_DOWNLOAD_URL ||
  "https://github.com/bagdanchik007/FitTrak/releases/latest";

/** Primary destinations — bottom bar on mobile, top of sidebar on desktop */
const primaryNav = [
  { to: "/dashboard", label: "Home", short: "Home" },
  { to: "/workouts", label: "Workouts", short: "Train" },
  { to: "/coach", label: "Coach", short: "Coach" },
  { to: "/live", label: "Live", short: "Live" },
] as const;

/** Secondary — sidebar (desktop) / “More” drawer (mobile) */
const moreNav = [
  { to: "/goals", label: "Goals" },
  { to: "/streaks", label: "Streaks" },
  { to: "/journal", label: "Journal" },
  { to: "/body-weight", label: "Weight" },
  { to: "/exercises", label: "Exercises" },
  { to: "/notifications", label: "Alerts" },
  { to: "/preferences", label: "Settings" },
  { to: "/templates", label: "Templates" },
] as const;

const sideLink = ({ isActive }: { isActive: boolean }) =>
  `flex items-center gap-2 rounded-lg px-3 py-2.5 text-sm font-medium transition ${
    isActive ? "bg-brand-600 text-white" : "text-slate-300 hover:bg-slate-800"
  }`;

const bottomLink = ({ isActive }: { isActive: boolean }) =>
  `flex flex-1 flex-col items-center justify-center gap-0.5 py-2 text-[10px] font-medium transition ${
    isActive ? "text-brand-500" : "text-slate-400"
  }`;

export function Layout() {
  const navigate = useNavigate();
  const location = useLocation();
  const authed = isAuthenticated();
  const [moreOpen, setMoreOpen] = useState(false);

  useEffect(() => {
    setMoreOpen(false);
  }, [location.pathname]);

  useEffect(() => {
    document.body.style.overflow = moreOpen ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [moreOpen]);

  function handleLogout() {
    logout();
    setMoreOpen(false);
    navigate("/login");
  }

  const isAuthPage =
    location.pathname === "/login" || location.pathname === "/register";

  return (
    <div className="min-h-screen min-h-[100dvh] flex bg-slate-950 text-slate-100">
      {/* ——— Desktop sidebar (laptop / computer) ——— */}
      {authed && (
        <aside className="hidden lg:flex lg:w-56 xl:w-64 shrink-0 flex-col border-r border-slate-800 bg-slate-900/90">
          <div className="px-4 py-5">
            <Link to="/dashboard" className="text-xl font-semibold text-brand-500">
              FitTrack
            </Link>
            <p className="mt-1 text-xs text-slate-500">Desktop app shell</p>
          </div>
          <nav className="flex-1 overflow-y-auto px-2 space-y-0.5">
            <p className="px-3 py-2 text-[10px] uppercase tracking-wider text-slate-500">
              Main
            </p>
            {primaryNav.map((item) => (
              <NavLink key={item.to} to={item.to} className={sideLink}>
                {item.label}
              </NavLink>
            ))}
            <p className="px-3 pt-4 py-2 text-[10px] uppercase tracking-wider text-slate-500">
              More
            </p>
            {moreNav.map((item) => (
              <NavLink key={item.to} to={item.to} className={sideLink}>
                {item.label}
              </NavLink>
            ))}
          </nav>
          <div className="border-t border-slate-800 p-3">
            <a
              href={RELEASES_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="mb-2 block w-full rounded-lg px-3 py-2 text-left text-sm text-brand-500 hover:bg-slate-800"
            >
              Download / releases
            </a>
            <button
              type="button"
              onClick={handleLogout}
              className="w-full rounded-lg px-3 py-2.5 text-left text-sm text-slate-400 hover:bg-slate-800 hover:text-white"
            >
              Logout
            </button>
          </div>
        </aside>
      )}

      <div className="flex min-w-0 flex-1 flex-col">
        {/* Top bar — mobile / tablet always; desktop only when guest */}
        <header
          className={`sticky top-0 z-30 border-b border-slate-800 bg-slate-900/90 backdrop-blur safe-top ${
            authed ? "lg:hidden" : ""
          }`}
        >
          <div className="mx-auto flex max-w-5xl items-center justify-between gap-3 px-4 py-3">
            <Link to={authed ? "/dashboard" : "/"} className="text-lg font-semibold text-brand-500">
              FitTrack
            </Link>
            {!authed && (
              <nav className="flex gap-1">
                <NavLink to="/login" className={sideLink}>
                  Login
                </NavLink>
                <NavLink to="/register" className={sideLink}>
                  Register
                </NavLink>
              </nav>
            )}
            {authed && (
              <button
                type="button"
                className="rounded-lg px-3 py-2 text-sm text-slate-300 hover:bg-slate-800 lg:hidden"
                onClick={() => setMoreOpen(true)}
                aria-label="Open more menu"
              >
                More
              </button>
            )}
          </div>
        </header>

        {/* Guest desktop top bar */}
        {!authed && (
          <header className="hidden lg:block sticky top-0 z-30 border-b border-slate-800 bg-slate-900/90 backdrop-blur">
            <div className="mx-auto flex max-w-5xl items-center justify-between px-4 py-3">
              <Link to="/" className="text-lg font-semibold text-brand-500">
                FitTrack
              </Link>
              <nav className="flex gap-1">
                <NavLink to="/login" className={sideLink}>
                  Login
                </NavLink>
                <NavLink to="/register" className={sideLink}>
                  Register
                </NavLink>
              </nav>
            </div>
          </header>
        )}

        <main
          className={`mx-auto w-full max-w-5xl flex-1 px-4 py-6 sm:py-8 ${
            authed && !isAuthPage ? "pb-24 lg:pb-8" : ""
          }`}
        >
          <Outlet />
        </main>

        {/* ——— Mobile bottom navigation ——— */}
        {authed && (
          <nav
            className="fixed inset-x-0 bottom-0 z-30 flex border-t border-slate-800 bg-slate-900/95 backdrop-blur safe-bottom lg:hidden"
            aria-label="Primary"
          >
            {primaryNav.map((item) => (
              <NavLink key={item.to} to={item.to} className={bottomLink}>
                <span className="text-base leading-none" aria-hidden>
                  {item.short === "Home"
                    ? "⌂"
                    : item.short === "Train"
                      ? "◈"
                      : item.short === "Coach"
                        ? "✦"
                        : "●"}
                </span>
                {item.short}
              </NavLink>
            ))}
            <button
              type="button"
              className={`flex flex-1 flex-col items-center justify-center gap-0.5 py-2 text-[10px] font-medium ${
                moreOpen ? "text-brand-500" : "text-slate-400"
              }`}
              onClick={() => setMoreOpen(true)}
            >
              <span className="text-base leading-none" aria-hidden>
                ☰
              </span>
              More
            </button>
          </nav>
        )}

        {/* Mobile “More” sheet */}
        {moreOpen && authed && (
          <>
            <div
              className="fixed inset-0 z-40 bg-black/60 lg:hidden"
              aria-hidden
              onClick={() => setMoreOpen(false)}
            />
            <div className="fixed inset-x-0 bottom-0 z-50 max-h-[75dvh] overflow-y-auto rounded-t-2xl border border-slate-700 bg-slate-900 p-4 safe-bottom lg:hidden">
              <div className="mb-3 flex items-center justify-between">
                <p className="text-sm font-medium text-slate-200">More</p>
                <button
                  type="button"
                  className="rounded-lg px-2 py-1 text-sm text-slate-400"
                  onClick={() => setMoreOpen(false)}
                >
                  Close
                </button>
              </div>
              <nav className="space-y-0.5">
                {moreNav.map((item) => (
                  <NavLink key={item.to} to={item.to} className={sideLink}>
                    {item.label}
                  </NavLink>
                ))}
                <button
                  type="button"
                  onClick={handleLogout}
                  className="mt-2 w-full rounded-lg px-3 py-2.5 text-left text-sm text-red-400 hover:bg-slate-800"
                >
                  Logout
                </button>
              </nav>
            </div>
          </>
        )}

        <footer className="hidden border-t border-slate-800 py-3 text-center text-xs text-slate-500 lg:block">
          FitTrack · same API · desktop sidebar + mobile app shell · v1.3
        </footer>
      </div>
    </div>
  );
}
