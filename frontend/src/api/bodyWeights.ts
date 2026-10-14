import { apiFetch } from "./client";

export type BodyWeight = {
  id: string;
  weight_kg: number;
  recorded_at: string;
};

export function fetchBodyWeights(): Promise<BodyWeight[]> {
  return apiFetch<BodyWeight[]>("/body-weights?limit=30");
}

export function fetchWeekDelta(): Promise<{ delta_kg: number | null; samples?: number }> {
  return apiFetch("/body-weights/week-delta");
}
