export function passwordHints(password: string): string[] {
  const hints: string[] = [];
  if (password.length > 0 && password.length < 12) hints.push("Use 12+ characters");
  if (password && (password === password.toLowerCase() || password === password.toUpperCase())) {
    hints.push("Mix upper and lower case");
  }
  if (password && !/\d/.test(password)) hints.push("Add a number");
  return hints;
}
