import re
from .errors import ErrorReason


def validate_name(name: str):
    if not name.strip():
        raise ValueError(ErrorReason.EMPTY_NAME.value)

    if not re.match(r"^[a-zA-Z][\w.-]*$", name):
        raise ValueError(ErrorReason.INVALID_NAME_CHARS.value)
