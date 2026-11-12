import { apiFetch } from "./client";

export type Preferences = {
  id?: string;
  weight_unit?: string;
  language?: string;
  weekly_goal_workouts?: number;
  email_reminders?: boolean;
  [key: string]: unknown;
};

export function fetchPreferences(): Promise<Preferences> {
  return apiFetch<Preferences>("/preferences/me");
}

export function fetchEffectivePreferences(): Promise<Record<string, unknown>> {
  return apiFetch("/preferences/me/effective");
}

export function updatePreferences(body: {
  weight_unit?: string;
  language?: string;
  weekly_goal_workouts?: number;
  email_reminders?: boolean;
}): Promise<Preferences> {
  return apiFetch<Preferences>("/preferences/me", {
    method: "PUT",
    body: JSON.stringify(body),
  });
}

export function resetPreferences(): Promise<Preferences> {
  return apiFetch<Preferences>("/preferences/me/reset", { method: "POST" });
}
