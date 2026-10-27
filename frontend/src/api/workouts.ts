import { apiFetch } from "./client";
import type { Workout } from "../types/api";

export function fetchWorkouts(limit = 20): Promise<Workout[]> {
  return apiFetch<Workout[]>(`/workouts?limit=${limit}`);
}

export type CreateWorkoutPayload = {
  title: string;
  performed_at: string;
  duration_minutes?: number | null;
  notes?: string | null;
  sets?: unknown[];
};

export function createWorkout(body: CreateWorkoutPayload): Promise<Workout> {
  return apiFetch<Workout>("/workouts", {
    method: "POST",
    body: JSON.stringify({ ...body, sets: body.sets ?? [] }),
  });
}
