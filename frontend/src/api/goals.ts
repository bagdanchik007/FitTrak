import { apiFetch } from "./client";

export type Goal = {
  id: string;
  title: string;
  target_value?: number | null;
  current_value?: number | null;
  unit?: string | null;
  is_completed?: boolean;
  deadline?: string | null;
};

export function fetchGoals(): Promise<Goal[]> {
  return apiFetch<Goal[]>("/goals");
}

export function fetchGoalsWithProgress(): Promise<Record<string, unknown>[]> {
  return apiFetch("/goals/with-progress");
}
