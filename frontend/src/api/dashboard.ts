import { apiFetch } from "./client";
import type { Dashboard, Workout } from "../types/api";

export function fetchDashboard(): Promise<Dashboard> {
  return apiFetch<Dashboard>("/stats/dashboard");
}

export function fetchWorkouts(): Promise<Workout[]> {
  return apiFetch<Workout[]>("/workouts?limit=20");
}

export function fetchStreak(): Promise<Record<string, unknown>> {
  return apiFetch("/streaks/me");
}
