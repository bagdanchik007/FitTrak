"""Clamp a number into [lo, hi]."""

def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))
