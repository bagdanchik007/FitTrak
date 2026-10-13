import { getAccessToken } from "../lib/auth";
import { apiFetch } from "./client";

export function fetchLiveStatus(): Promise<{ active: boolean; session: Record<string, unknown> | null }> {
  return apiFetch("/live-session/status");
}

export function openLiveSessionSocket(): WebSocket | null {
  const token = getAccessToken();
  if (!token) return null;
  const proto = window.location.protocol === "https:" ? "wss" : "ws";
  // Dev: backend on 8000; production would share host
  const host = import.meta.env.VITE_WS_HOST ?? "localhost:8000";
  const url = `${proto}://${host}/api/v1/ws/live-session?token=${encodeURIComponent(token)}`;
  return new WebSocket(url);
}
