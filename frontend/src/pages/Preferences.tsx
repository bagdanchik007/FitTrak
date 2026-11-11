import { useEffect, useState } from "react";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import { fetchEffectivePreferences, fetchPreferences } from "../api/preferences";
import { isAuthenticated } from "../lib/auth";
import { ErrorBanner } from "../components/ErrorBanner";
import { softDeleteConfirmLabel, softDeleteWarning } from "../lib/softDeleteCopy";

export function Preferences() {
  useDocumentTitle("Settings");
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
      {error && <ErrorBanner message={error} onDismiss={() => setError(null)} />}
      <pre className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 text-xs overflow-auto">
        {JSON.stringify({ stored: prefs, effective }, null, 2)}
      </pre>
    
      <section className="mt-8 rounded-xl border border-red-900/40 bg-red-950/20 p-4 text-sm">
        <p className="font-medium text-red-300">{softDeleteConfirmLabel()}</p>
        <p className="mt-1 text-slate-400">{softDeleteWarning()}</p>
      </section>
</div>
  );
}
