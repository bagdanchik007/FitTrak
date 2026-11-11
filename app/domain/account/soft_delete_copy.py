"""User-facing copy for account soft-delete flows."""

def soft_delete_warning() -> str:
    return "Your account will be deactivated and can no longer sign in."


def soft_delete_confirm_label() -> str:
    return "Deactivate account"
