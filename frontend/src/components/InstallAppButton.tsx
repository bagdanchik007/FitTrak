import { useEffect, useState } from "react";

/** Chromium beforeinstallprompt event (not in standard TS lib). */
interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: "accepted" | "dismissed" }>;
}

type Props = {
  className?: string;
  /** GitHub release or zip URL for “download source / desktop package” */
  downloadUrl?: string;
};

const DEFAULT_DOWNLOAD =
  import.meta.env.VITE_APP_DOWNLOAD_URL ||
  "https://github.com/bagdanchik007/FitTrak/releases/latest";

export function InstallAppButton({ className = "", downloadUrl = DEFAULT_DOWNLOAD }: Props) {
  const [deferred, setDeferred] = useState<BeforeInstallPromptEvent | null>(null);
  const [installed, setInstalled] = useState(false);
  const [hint, setHint] = useState<string | null>(null);

  useEffect(() => {
    const isStandalone =
      window.matchMedia("(display-mode: standalone)").matches ||
      // iOS Safari
      ("standalone" in navigator && (navigator as { standalone?: boolean }).standalone === true);
    if (isStandalone) {
      setInstalled(true);
      return;
    }

    const onBip = (e: Event) => {
      e.preventDefault();
      setDeferred(e as BeforeInstallPromptEvent);
    };
    window.addEventListener("beforeinstallprompt", onBip);
    window.addEventListener("appinstalled", () => {
      setInstalled(true);
      setDeferred(null);
    });
    return () => window.removeEventListener("beforeinstallprompt", onBip);
  }, []);

  async function handleInstall() {
    if (deferred) {
      await deferred.prompt();
      const { outcome } = await deferred.userChoice;
      if (outcome === "accepted") {
        setInstalled(true);
      }
      setDeferred(null);
      return;
    }
    // iOS / browsers without beforeinstallprompt
    const ua = navigator.userAgent;
    if (/iPhone|iPad|iPod/i.test(ua)) {
      setHint("Auf dem iPhone: Teilen → „Zum Home-Bildschirm“ tippen.");
    } else if (/Android/i.test(ua)) {
      setHint("Im Browser-Menü „App installieren“ oder „Zum Startbildschirm“ wählen.");
    } else {
      setHint("Im Browser-Menü nach „App installieren“ suchen — oder unten die Release-Datei laden.");
    }
  }

  if (installed) {
    return (
      <p className={`text-sm text-slate-400 ${className}`}>App ist installiert ✓</p>
    );
  }

  return (
    <div className={`flex flex-col gap-2 sm:flex-row sm:flex-wrap sm:items-center ${className}`}>
      <button
        type="button"
        onClick={handleInstall}
        className="rounded-lg bg-brand-600 px-4 py-2.5 text-sm font-semibold text-white hover:bg-brand-700 touch-target"
      >
        {deferred ? "App installieren" : "App herunterladen / installieren"}
      </button>
      <a
        href={downloadUrl}
        target="_blank"
        rel="noopener noreferrer"
        className="rounded-lg border border-slate-600 px-4 py-2.5 text-center text-sm text-slate-200 hover:bg-slate-800"
      >
        Release / ZIP herunterladen
      </a>
      {hint && <p className="w-full text-xs text-slate-400">{hint}</p>}
    </div>
  );
}
