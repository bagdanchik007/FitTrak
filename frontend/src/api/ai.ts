import { apiFetch } from "./client";

export type WorkoutSuggestion = {
  focus: string;
  experience: string;
  exercises: { name: string; sets: number; reps: string; rest_seconds: number }[];
  notes: string;
  engine: string;
};

export function suggestWorkout(body: {
  recent_focuses?: string[];
  experience?: string;
  focus?: string;
}): Promise<WorkoutSuggestion> {
  return apiFetch("/ai/suggest-workout", {
    method: "POST",
    body: JSON.stringify(body),
  });
}

export function askCoach(message: string): Promise<{ reply: string; engine: string }> {
  return apiFetch("/ai/coach", {
    method: "POST",
    body: JSON.stringify({ message }),
  });
}
