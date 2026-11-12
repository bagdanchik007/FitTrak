import { apiFetch } from "./client";
import { clearTokens } from "../lib/auth";

export async function changePassword(current_password: string, new_password: string): Promise<void> {
  await apiFetch<void>("/auth/change-password", {
    method: "POST",
    body: JSON.stringify({ current_password, new_password }),
  });
}

export async function softDeleteAccount(): Promise<void> {
  await apiFetch<{ status: string }>("/users/me/soft-delete", { method: "POST" });
  clearTokens();
}
