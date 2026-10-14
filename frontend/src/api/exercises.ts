import { apiFetch } from "./client";

export type Exercise = {
  id: string;
  name: string;
  muscle_group?: string | null;
};

export function fetchExercises(): Promise<Exercise[]> {
  return apiFetch<Exercise[]>("/exercises?limit=50");
}
