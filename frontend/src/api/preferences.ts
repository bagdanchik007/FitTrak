import { apiFetch } from "./client";

export function fetchPreferences(): Promise<Record<string, unknown>> {
  return apiFetch("/preferences/me");
}

export function fetchEffectivePreferences(): Promise<Record<string, unknown>> {
  return apiFetch("/preferences/me/effective");
}
