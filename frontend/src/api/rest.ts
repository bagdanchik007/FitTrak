import { apiFetch } from "./client";

export function fetchRestSuggestion(rpe?: number, isCompound = true) {
  const params = new URLSearchParams();
  if (rpe != null) params.set("rpe", String(rpe));
  params.set("is_compound", String(isCompound));
  return apiFetch<{ rest_seconds: number }>(`/meta/rest-suggestion?${params}`);
}
