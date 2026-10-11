import { FormEvent, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { login, register } from "../api/auth";

export function Register() {
  const navigate = useNavigate();
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      await register(email, password, fullName);
      await login(email, password);
      navigate("/dashboard");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Registration failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mx-auto max-w-md">
      <h1 className="text-2xl font-bold">Create account</h1>
      <p className="mt-1 text-sm text-slate-400">
        Already registered? <Link className="text-brand-500 hover:underline" to="/login">Sign in</Link>
      </p>
      <form onSubmit={onSubmit} className="mt-6 space-y-4">
        <label className="block text-sm">
          <span className="text-slate-400">Full name</span>
          <input
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-900 px-3 py-2"
            value={fullName}
            onChange={(e) => setFullName(e.target.value)}
          />
        </label>
        <label className="block text-sm">
          <span className="text-slate-400">Email</span>
          <input
            type="email"
            required
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-900 px-3 py-2"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <label className="block text-sm">
          <span className="text-slate-400">Password</span>
          <input
            type="password"
            required
            minLength={8}
            className="mt-1 w-full rounded-lg border border-slate-700 bg-slate-900 px-3 py-2"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        {error && <p className="text-sm text-red-400">{error}</p>}
        <button
          type="submit"
          disabled={loading}
          className="w-full rounded-lg bg-brand-600 py-2 text-sm font-semibold hover:bg-brand-700 disabled:opacity-50"
        >
          {loading ? "Creating…" : "Register"}
        </button>
      </form>
    </div>
  );
}
