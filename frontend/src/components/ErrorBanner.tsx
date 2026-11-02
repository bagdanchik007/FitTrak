type Props = { message: string; onDismiss?: () => void };

export function ErrorBanner({ message, onDismiss }: Props) {
  if (!message) return null;
  return (
    <div
      role="alert"
      className="flex items-start justify-between gap-3 rounded-lg border border-red-900/60 bg-red-950/40 px-3 py-2 text-sm text-red-300"
    >
      <span>{message}</span>
      {onDismiss && (
        <button type="button" className="text-xs text-red-400 hover:text-red-200" onClick={onDismiss}>
          Dismiss
        </button>
      )}
    </div>
  );
}
