import { apiFetch } from "./client";

export type Notification = {
  kind: string;
  title: string;
  body: string;
  created_at: string;
};

export function fetchNotifications(): Promise<Notification[]> {
  return apiFetch<Notification[]>("/notifications");
}
