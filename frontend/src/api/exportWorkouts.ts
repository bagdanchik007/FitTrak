import { getAccessToken } from "../lib/auth";

const API_BASE = import.meta.env.VITE_API_BASE ?? "http://127.0.0.1:8000/api/v1";

/** Download workouts CSV via authenticated fetch (blob). */
export async function downloadWorkoutsCsv(): Promise<void> {
  const token = getAccessToken();
  const res = await fetch(`${API_BASE}/workouts/export/csv`, {
    headers: token ? { Authorization: `Bearer ${token}` } : {},
  });
  if (!res.ok) {
    throw new Error(`Export failed (${res.status})`);
  }
  const blob = await res.blob();
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "workouts.csv";
  a.click();
  URL.revokeObjectURL(url);
}
