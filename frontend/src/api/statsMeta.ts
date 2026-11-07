import { apiFetch } from "./client";

export function fetchVolumeSummary(volumes: number[]) {
  const q = volumes.join(",");
  return apiFetch<{ avg: number | null; max: number | null; min: number | null; count: number }>(
    `/meta/volume-summary?volumes=${encodeURIComponent(q)}`,
  );
}
