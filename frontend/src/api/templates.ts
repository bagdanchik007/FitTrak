import { apiFetch } from "./client";

export type Template = {
  id: string;
  name?: string;
  title?: string;
  [key: string]: unknown;
};

export function fetchTemplates(): Promise<Template[]> {
  return apiFetch<Template[]>("/templates?limit=30");
}
