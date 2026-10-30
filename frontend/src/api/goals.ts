import { apiFetch } from "./client";

export type Goal = {
  id: string;
  title?: string;
  target_value?: number | null;
  current_value?: number | null;
  unit?: string | null;
  percent_complete?: number | null;
  status?: string;
  is_completed?: boolean;
  [key: string]: unknown;
};

export function fetchGoals(): Promise<Goal[]> {
  return apiFetch<Goal[]>("/goals?limit=30");
}

export function fetchGoalsWithProgress(): Promise<Goal[]> {
  return apiFetch<Goal[]>("/goals/with-progress");
}

export function createGoal(body: {
  title: string;
  target_value?: number | null;
  unit?: string | null;
}): Promise<Goal> {
  return apiFetch<Goal>("/goals", {
    method: "POST",
    body: JSON.stringify(body),
  });
}
