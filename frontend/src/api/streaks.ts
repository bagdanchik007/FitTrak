import { apiFetch } from "./client";

export function fetchStreak(): Promise<Record<string, unknown>> {
  return apiFetch("/streaks/me");
}

export function fetchConsistency(): Promise<Record<string, unknown>> {
  return apiFetch("/streaks/me/consistency");
}
