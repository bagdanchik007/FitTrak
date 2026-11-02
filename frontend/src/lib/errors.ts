const MAP: Record<string, string> = {
  unauthorized: "Please sign in again.",
  not_found: "That item could not be found.",
  validation: "Please check your input and try again.",
  server: "Something went wrong. Try again shortly.",
};

export function friendlyError(codeOrMessage: string): string {
  const key = codeOrMessage.toLowerCase();
  return MAP[key] ?? codeOrMessage;
}
