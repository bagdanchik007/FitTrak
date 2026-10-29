import { apiFetch } from "./client";

export type Goal = {
  id: string;
  title?: string;
  name?: string;
  target_value?: number;
  current_value?: number;
  [key: string]: unknown;
};

export function fetchGoals(): Promise<Goal[]> {
  return apiFetch<Goal[]>("/goals?limit=30");
}

export function createGoal(body: {
  title: string;
  target_value?: number;
}): Promise<Goal> {
  return apiFetch<Goal>("/goals", {
    method: "POST",
    body: JSON.stringify(body),
  });
}
