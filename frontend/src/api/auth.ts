import { apiFetch } from "./client";
import type { TokenResponse, UserMe } from "../types/api";
import { setTokens, clearTokens } from "../lib/auth";

export async function login(email: string, password: string): Promise<TokenResponse> {
  const body = new URLSearchParams();
  body.set("username", email);
  body.set("password", password);
  const res = await fetch(`${import.meta.env.VITE_API_BASE ?? "/api/v1"}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body,
  });
  if (!res.ok) throw new Error(await res.text());
  const data = (await res.json()) as TokenResponse;
  setTokens(data.access_token, data.refresh_token);
  return data;
}

export async function register(email: string, password: string, fullName: string): Promise<void> {
  await apiFetch(
    "/auth/register",
    {
      method: "POST",
      body: JSON.stringify({ email, password, full_name: fullName }),
    },
    false
  );
}

export async function me(): Promise<UserMe> {
  return apiFetch<UserMe>("/users/me");
}

export function logout(): void {
  clearTokens();
}
