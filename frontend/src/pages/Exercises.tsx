import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { fetchExercises, type Exercise } from "../api/exercises";
import { isAuthenticated } from "../lib/auth";

export function Exercises() {
  const navigate = useNavigate();
  const [items, setItems] = useState<Exercise[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    fetchExercises()
      .then(setItems)
      .catch((e) => setError(e instanceof Error ? e.message : "Failed"));
  }, [navigate]);

  return (
    <div className="space-y-4">
      <h1 className="text-2xl font-bold">Exercises</h1>
      {error && <p className="text-sm text-red-400">{error}</p>}
      <ul className="grid gap-2 sm:grid-cols-2">
        {items.map((ex) => (
          <li key={ex.id} className="rounded-xl border border-slate-800 bg-slate-900/50 p-3">
            <p className="font-medium">{ex.name}</p>
            <p className="text-xs text-slate-500">{ex.muscle_group || "—"}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}
