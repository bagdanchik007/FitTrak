import { useEffect, useState } from "react"
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import { fetchConsistency, fetchStreak } from "../api/streaks";
import { isAuthenticated } from "../lib/auth";
import { ErrorBanner } from "../components/ErrorBanner";
import { LoadingBlock } from "../components/LoadingBlock";
import { StatCard } from "../components/StatCard";

export function Streaks() {
  useDocumentTitle("Streaks");
  const navigate = useNavigate();
  const [streak, setStreak] = useState<Record<string, unknown> | null>(null);
  const [consistency, setConsistency] = useState<Record<string, unknown> | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    Promise.all([fetchStreak(), fetchConsistency()])
      .then(([s, c]) => {
        setStreak(s);
        setConsistency(c);
      })
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Streaks</h1>
      {error && <ErrorBanner message={error} onDismiss={() => setError(null)} />}
      {!streak && !error && <LoadingBlock label="Loading streaks…" />}
      <div className="grid gap-4 sm:grid-cols-2">
        <StatCard label="Current streak" value={String(streak?.current_streak ?? "—")} />
        <StatCard
          label="Consistency"
          value={consistency?.score != null ? String(consistency.score) : "—"}
          hint={String(consistency?.band ?? "")}
        />
      </div>
    </div>
  );
}
