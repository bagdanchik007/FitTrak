import { apiFetch } from "./client";

export function calcCalories(weightKg: number, durationMinutes: number, activity = "general") {
  const q = new URLSearchParams({
    weight_kg: String(weightKg),
    duration_minutes: String(durationMinutes),
    activity,
  });
  return apiFetch<{ kcal: number; met: number; activity: string }>(`/health-calc/calories?${q}`);
}

export function calcSteps(params: {
  steps?: number;
  distance_km?: number;
  height_cm?: number;
  weight_kg?: number;
}) {
  const q = new URLSearchParams();
  if (params.steps != null) q.set("steps", String(params.steps));
  if (params.distance_km != null) q.set("distance_km", String(params.distance_km));
  if (params.height_cm != null) q.set("height_cm", String(params.height_cm));
  if (params.weight_kg != null) q.set("weight_kg", String(params.weight_kg));
  return apiFetch<{ steps: number; distance_km: number; kcal_estimate: number }>(
    `/health-calc/steps?${q}`,
  );
}

export function listCalcActivities() {
  return apiFetch<{ activities: string[]; mets: Record<string, number> }>("/health-calc/activities");
}
