from enum import StrEnum


class ErrorReason(StrEnum):
    # Exit
    NO_VALUES_PROVIDED = "No name or repo provided"

    # Name
    EMPTY_NAME = "Name must not be empty"
    INVALID_NAME_CHARS = "Name contains invalid characters"
