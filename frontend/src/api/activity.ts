import { apiFetch } from "./client";

export type ActivityItem = {
  type: string;
  title: string;
  occurred_on: string;
  meta?: { label?: string; [key: string]: unknown } | null;
};

export function fetchActivity(limit = 20): Promise<ActivityItem[]> {
  return apiFetch<ActivityItem[]>(`/activity/feed?limit=${limit}`);
}
