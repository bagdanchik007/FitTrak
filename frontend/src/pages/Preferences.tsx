import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchEffectivePreferences, fetchPreferences } from "../api/preferences";
import { isAuthenticated } from "../lib/auth";

export function Preferences() {
  const navigate = useNavigate();
  const [prefs, setPrefs] = useState<Record<string, unknown> | null>(null);
  const [effective, setEffective] = useState<Record<string, unknown> | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    Promise.all([fetchPreferences(), fetchEffectivePreferences()])
      .then(([p, e]) => {
        setPrefs(p);
        setEffective(e);
      })
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Preferences</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <pre className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 text-xs overflow-auto">
        {JSON.stringify({ stored: prefs, effective }, null, 2)}
      </pre>
    </div>
  );
}
