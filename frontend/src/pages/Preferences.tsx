import { FormEvent, useEffect, useState } from "react";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import {
  fetchEffectivePreferences,
  fetchPreferences,
  resetPreferences,
  updatePreferences,
  type Preferences as Prefs,
} from "../api/preferences";
import { changePassword, softDeleteAccount } from "../api/account";
import { isAuthenticated } from "../lib/auth";
import { ErrorBanner } from "../components/ErrorBanner";
import { softDeleteConfirmLabel, softDeleteWarning } from "../lib/softDeleteCopy";

export function Preferences() {
  useDocumentTitle("Settings");
  const navigate = useNavigate();
  const [prefs, setPrefs] = useState<Prefs | null>(null);
  const [effective, setEffective] = useState<Record<string, unknown> | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [saving, setSaving] = useState(false);
  const [unit, setUnit] = useState("kg");
  const [language, setLanguage] = useState("en");
  const [weeklyGoal, setWeeklyGoal] = useState(3);
  const [reminders, setReminders] = useState(false);
  const [currentPw, setCurrentPw] = useState("");
  const [newPw, setNewPw] = useState("");
  const [pwMsg, setPwMsg] = useState<string | null>(null);

  function load() {
    Promise.all([fetchPreferences(), fetchEffectivePreferences()])
      .then(([p, e]) => {
        setPrefs(p);
        setEffective(e);
        setUnit(String(p.weight_unit ?? "kg"));
        setLanguage(String(p.language ?? "en"));
        setWeeklyGoal(Number(p.weekly_goal_workouts ?? 3));
        setReminders(Boolean(p.email_reminders));
      })
      .catch((err) => setError(err instanceof Error ? err.message : "Failed"));
  }

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    load();
  }, [navigate]);

  async function onSave(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setSaving(true);
    try {
      await updatePreferences({
        weight_unit: unit,
        language,
        weekly_goal_workouts: weeklyGoal,
        email_reminders: reminders,
      });
      load();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Save failed");
    } finally {
      setSaving(false);
    }
  }

  async function onReset() {
    setError(null);
    setSaving(true);
    try {
      await resetPreferences();
      load();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Reset failed");
    } finally {
      setSaving(false);
    }
  }

  async function onChangePassword(e: FormEvent) {
    e.preventDefault();
    setPwMsg(null);
    setError(null);
    try {
      await changePassword(currentPw, newPw);
      setCurrentPw("");
      setNewPw("");
      setPwMsg("Password updated.");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Password change failed");
    }
  }

  async function onSoftDelete() {
    if (!window.confirm(`${softDeleteWarning()}\n\nContinue?`)) return;
    setError(null);
    try {
      await softDeleteAccount();
      navigate("/login");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not deactivate account");
    }
  }

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Preferences</h1>
      {error && <ErrorBanner message={error} onDismiss={() => setError(null)} />}

      <form onSubmit={onSave} className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <h2 className="text-sm font-medium text-slate-300">Training defaults</h2>
        <label className="block text-sm">
          <span className="text-slate-400">Weight unit</span>
          <select
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
            value={unit}
            onChange={(e) => setUnit(e.target.value)}
          >
            <option value="kg">kg</option>
            <option value="lbs">lbs</option>
          </select>
        </label>
        <label className="block text-sm">
          <span className="text-slate-400">Language</span>
          <select
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
          >
            <option value="en">English</option>
            <option value="de">Deutsch</option>
            <option value="uk">Українська</option>
            <option value="pl">Polski</option>
          </select>
        </label>
        <label className="block text-sm">
          <span className="text-slate-400">Weekly workout goal</span>
          <input
            type="number"
            min={1}
            max={14}
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2"
            value={weeklyGoal}
            onChange={(e) => setWeeklyGoal(Number(e.target.value))}
          />
        </label>
        <label className="flex items-center gap-2 text-sm text-slate-300">
          <input
            type="checkbox"
            checked={reminders}
            onChange={(e) => setReminders(e.target.checked)}
          />
          Email reminders
        </label>
        <div className="flex flex-wrap gap-2">
          <button
            type="submit"
            disabled={saving}
            className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium hover:bg-brand-700 disabled:opacity-50"
          >
            {saving ? "Saving…" : "Save preferences"}
          </button>
          <button
            type="button"
            onClick={onReset}
            disabled={saving}
            className="rounded-lg border border-slate-700 px-4 py-2 text-sm hover:bg-slate-800 disabled:opacity-50"
          >
            Reset defaults
          </button>
        </div>
      </form>

      <form onSubmit={onChangePassword} className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <h2 className="text-sm font-medium text-slate-300">Change password</h2>
        {pwMsg && <p className="text-sm text-emerald-400">{pwMsg}</p>}
        <input
          type="password"
          required
          minLength={8}
          placeholder="Current password"
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          value={currentPw}
          onChange={(e) => setCurrentPw(e.target.value)}
        />
        <input
          type="password"
          required
          minLength={8}
          placeholder="New password"
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          value={newPw}
          onChange={(e) => setNewPw(e.target.value)}
        />
        <button
          type="submit"
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium hover:bg-brand-700"
        >
          Update password
        </button>
      </form>

      {effective && (
        <details className="rounded-xl border border-slate-800 bg-slate-900/40 p-4 text-xs text-slate-400">
          <summary className="cursor-pointer text-slate-300">Effective preferences (debug)</summary>
          <pre className="mt-2 overflow-auto">{JSON.stringify({ stored: prefs, effective }, null, 2)}</pre>
        </details>
      )}

      <section className="rounded-xl border border-red-900/40 bg-red-950/20 p-4 text-sm">
        <p className="font-medium text-red-300">{softDeleteConfirmLabel()}</p>
        <p className="mt-1 text-slate-400">{softDeleteWarning()}</p>
        <button
          type="button"
          onClick={onSoftDelete}
          className="mt-3 rounded-lg border border-red-800 px-3 py-1.5 text-sm text-red-300 hover:bg-red-950"
        >
          {softDeleteConfirmLabel()}
        </button>
      </section>
    </div>
  );
}
