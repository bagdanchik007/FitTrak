import { FormEvent, useEffect, useState } from "react";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import { createJournalEntry, fetchJournal, type JournalEntry } from "../api/journal";
import { isAuthenticated } from "../lib/auth";
import { EmptyState } from "../components/EmptyState";
import { ErrorBanner } from "../components/ErrorBanner";

export function Journal() {
  useDocumentTitle("Journal");
  const navigate = useNavigate();
  const [items, setItems] = useState<JournalEntry[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [mood, setMood] = useState("");
  const [saving, setSaving] = useState(false);

  function load() {
    fetchJournal()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    load();
  }, [navigate]);

  async function onCreate(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setSaving(true);
    try {
      await createJournalEntry({
        title: title.trim(),
        body: body.trim(),
        mood: mood.trim() || null,
      });
      setTitle("");
      setBody("");
      setMood("");
      load();
    } catch (err) {
      setError(err instanceof Error ? err.message : "Could not save entry");
    } finally {
      setSaving(false);
    }
  }

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Journal</h1>
      {error && <ErrorBanner message={error} onDismiss={() => setError(null)} />}
      <form onSubmit={onCreate} className="space-y-3 rounded-xl border border-slate-800 bg-slate-900/50 p-4">
        <h2 className="text-sm font-medium text-slate-300">New entry</h2>
        <input
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          placeholder="Title"
          required
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <textarea
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          placeholder="How did training feel?"
          required
          rows={3}
          value={body}
          onChange={(e) => setBody(e.target.value)}
        />
        <input
          className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 text-sm"
          placeholder="Mood (optional)"
          value={mood}
          onChange={(e) => setMood(e.target.value)}
        />
        <button
          type="submit"
          disabled={saving}
          className="rounded-lg bg-brand-600 px-4 py-2 text-sm font-medium hover:bg-brand-700 disabled:opacity-50"
        >
          {saving ? "Saving…" : "Add entry"}
        </button>
      </form>
      <ul className="space-y-2">
        {items.length === 0 && !error && (
          <li>
            <EmptyState title="No journal entries yet" hint="Log how training felt after a session." />
          </li>
        )}
        {items.map((e) => (
          <li key={e.id} className="rounded-xl border border-slate-800 bg-slate-900/50 p-4">
            <p className="text-xs text-slate-500">{e.created_at}</p>
            <p className="font-medium">{e.title}</p>
            {e.mood && <p className="text-sm text-brand-500">{e.mood}</p>}
            <p className="text-sm text-slate-300">{e.body || "—"}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
