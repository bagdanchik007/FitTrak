import { clearTokens, getAccessToken, getRefreshToken, setTokens } from "../lib/auth";
import type { TokenResponse } from "../types/api";

const API_BASE = import.meta.env.VITE_API_BASE ?? "/api/v1";

async function tryRefresh(): Promise<boolean> {
  const refresh = getRefreshToken();
  if (!refresh) return false;
  const res = await fetch(`${API_BASE}/auth/refresh`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ refresh_token: refresh }),
  });
  if (!res.ok) {
    clearTokens();
    return false;
  }
  const data = (await res.json()) as TokenResponse;
  setTokens(data.access_token, data.refresh_token);
  return true;
}

export async function apiFetch<T>(
  path: string,
  options: RequestInit = {},
  auth = true
): Promise<T> {
  const headers = new Headers(options.headers);
  if (!headers.has("Content-Type") && options.body) {
    headers.set("Content-Type", "application/json");
  }
  if (auth) {
    const token = getAccessToken();
    if (token) headers.set("Authorization", `Bearer ${token}`);
  }
  let res = await fetch(`${API_BASE}${path}`, { ...options, headers });
  if (res.status === 401 && auth) {
    const ok = await tryRefresh();
    if (ok) {
      headers.set("Authorization", `Bearer ${getAccessToken()}`);
      res = await fetch(`${API_BASE}${path}`, { ...options, headers });
    }
  }
  if (!res.ok) {
    const text = await res.text();
    throw new Error(text || `HTTP ${res.status}`);
  }
  if (res.status === 204) return undefined as T;
  return (await res.json()) as T;
}
