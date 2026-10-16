import { useEffect, useState } from "react";
import { Link, NavLink, Outlet, useLocation, useNavigate } from "react-router-dom";
import { logout } from "../api/auth";
import { isAuthenticated } from "../lib/auth";

const linkClass = ({ isActive }: { isActive: boolean }) =>
  `block w-full px-3 py-2.5 rounded-lg text-sm font-medium transition ${
    isActive ? "bg-brand-600 text-white" : "text-slate-300 hover:bg-slate-800"
  }`;

const navItems = [
  { to: "/dashboard", label: "Dashboard" },
  { to: "/workouts", label: "Workouts" },
  { to: "/goals", label: "Goals" },
  { to: "/streaks", label: "Streaks" },
  { to: "/live", label: "Live" },
  { to: "/journal", label: "Journal" },
  { to: "/body-weight", label: "Weight" },
  { to: "/exercises", label: "Exercises" },
  { to: "/notifications", label: "Alerts" },
  { to: "/preferences", label: "Prefs" },
  { to: "/coach", label: "Coach" },
] as const;

export function Layout() {
  const navigate = useNavigate();
  const location = useLocation();
  const authed = isAuthenticated();
  const [menuOpen, setMenuOpen] = useState(false);

  // Close mobile menu on route change
  useEffect(() => {
    setMenuOpen(false);
  }, [location.pathname]);

  // Prevent body scroll when drawer open
  useEffect(() => {
    document.body.style.overflow = menuOpen ? "hidden" : "";
    return () => {
      document.body.style.overflow = "";
    };
  }, [menuOpen]);

  function handleLogout() {
    logout();
    setMenuOpen(false);
    navigate("/login");
  }

  const navLinks = authed ? (
    <>
      {navItems.map((item) => (
        <NavLink key={item.to} to={item.to} className={linkClass}>
          {item.label}
        </NavLink>
      ))}
      <button
        type="button"
        className="mt-2 w-full px-3 py-2.5 text-left text-sm text-slate-400 hover:text-white rounded-lg hover:bg-slate-800 md:mt-0 md:w-auto md:ml-1"
        onClick={handleLogout}
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
  );

  return (
    <div className="min-h-screen min-h-[100dvh] flex flex-col bg-slate-950 text-slate-100">
      <header className="border-b border-slate-800 bg-slate-900/90 backdrop-blur sticky top-0 z-30 safe-top">
        <div className="mx-auto max-w-5xl flex items-center justify-between gap-3 px-4 py-3">
          <Link
            to="/"
            className="text-lg font-semibold tracking-tight text-brand-500 shrink-0"
          >
            FitTrack
          </Link>

          {/* Desktop nav */}
          <nav className="hidden md:flex md:flex-wrap md:items-center md:justify-end md:gap-0.5 max-w-[70%]">
            {navLinks}
          </nav>

          {/* Mobile menu button */}
          <button
            type="button"
            className="md:hidden inline-flex items-center justify-center rounded-lg p-2 text-slate-300 hover:bg-slate-800 hover:text-white focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500"
            aria-expanded={menuOpen}
            aria-controls="mobile-nav"
            aria-label={menuOpen ? "Close menu" : "Open menu"}
            onClick={() => setMenuOpen((o) => !o)}
          >
            {menuOpen ? (
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden>
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            ) : (
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" aria-hidden>
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            )}
          </button>
        </div>

        {/* Mobile drawer */}
        {menuOpen && (
          <>
            <div
              className="fixed inset-0 z-40 bg-black/60 md:hidden"
              aria-hidden
              onClick={() => setMenuOpen(false)}
            />
            <nav
              id="mobile-nav"
              className="fixed inset-y-0 right-0 z-50 w-[min(100%,18rem)] border-l border-slate-800 bg-slate-900 p-4 shadow-xl md:hidden flex flex-col gap-1 overflow-y-auto safe-bottom"
            >
              <p className="px-3 py-2 text-xs uppercase tracking-wide text-slate-500">Menu</p>
              {navLinks}
            </nav>
          </>
        )}
      </header>

      <main className="flex-1 mx-auto w-full max-w-5xl px-4 py-6 sm:py-8">
        <Outlet />
      </main>

      <footer className="border-t border-slate-800 py-4 px-4 text-center text-xs text-slate-500 safe-bottom">
        FitTrack · React + TypeScript + Tailwind · v1.0
      </footer>
    </div>
  );
}
