import { useEffect, useRef, useState } from "react";
import { useDocumentTitle } from "../hooks/useDocumentTitle";
import { useNavigate } from "react-router-dom";
import { openLiveSessionSocket } from "../api/live";
import { isAuthenticated } from "../lib/auth";

export function LiveSession(
  // titled
) {
  useDocumentTitle("Live");
  const navigate = useNavigate();
  const [status, setStatus] = useState("disconnected");
  const [session, setSession] = useState<Record<string, unknown> | null>(null);
  const [log, setLog] = useState<string[]>([]);
  const wsRef = useRef<WebSocket | null>(null);

  useEffect(() => {
    if (!isAuthenticated()) {
      navigate("/login");
      return;
    }
    const ws = openLiveSessionSocket();
    if (!ws) return;
    wsRef.current = ws;
    ws.onopen = () => setStatus("connected");
    ws.onclose = () => setStatus("disconnected");
    ws.onmessage = (ev) => {
      try {
        const data = JSON.parse(ev.data);
        setLog((prev) => [ev.data, ...prev].slice(0, 20));
        if (data.session) setSession(data.session);
      } catch {
        /* ignore */
      }
    };
    return () => ws.close();
  }, [navigate]);

  function send(event: string, extra: Record<string, unknown> = {}) {
    wsRef.current?.send(JSON.stringify({ event, ...extra }));
  }

  return (
    <div className="space-y-6">
      <div>
        <h1 className="text-2xl font-bold">Live session</h1>
        <p className="text-sm text-slate-400">
          WebSocket status: <span className="text-brand-500">{status}</span>
        </p>
      </div>
      <div className="flex flex-wrap gap-2">
        <button
          type="button"
          className="rounded-lg bg-brand-600 px-3 py-2 text-sm"
          onClick={() => send("set_logged", { exercise_name: "Bench Press" })}
        >
          Log set
        </button>
        <button
          type="button"
          className="rounded-lg border border-slate-700 px-3 py-2 text-sm"
          onClick={() => send("exercise_changed", { exercise_name: "Squat" })}
        >
          Change exercise
        </button>
        <button
          type="button"
          className="rounded-lg border border-slate-700 px-3 py-2 text-sm"
          onClick={() => send("ended")}
        >
          End session
        </button>
      </div>
      {session && (
        <div className="rounded-xl border border-slate-800 bg-slate-900/50 p-4 text-sm">
          <p>Sets: {String(session.set_count ?? 0)}</p>
          <p>Exercise: {String(session.exercise_name ?? "—")}</p>
          <p>Last event: {String(session.last_event ?? "—")}</p>
        </div>
      )}
      <div>
        <p className="text-xs uppercase text-slate-500 mb-2">Event log</p>
        <ul className="space-y-1 font-mono text-xs text-slate-400">
          {log.map((line, i) => (
            <li key={i} className="truncate">
              {line}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
