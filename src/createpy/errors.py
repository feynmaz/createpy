from enum import StrEnum


class ErrorReason(StrEnum):
    # Exit
    NO_VALUES_PROVIDED = "No name or repo provided"

    # Name
    EMPTY_NAME = "Name must not be empty"
    INVALID_NAME_CHARS = "Name contains invalid characters"

    # Repo
    EMPTY_REPO = "Repo must not be empty"
    INVALID_REPO_URL = "Invalid repo URL format"

    # Git user
    EMPTY_GIT_USER = "Git user name must not be empty"
    INVALID_GIT_USER = "Git user name contains invalid characters"
    GIT_USER_TOO_LONG = "Git user name exceeds 39 characters"

    # Git email
    EMPTY_GIT_EMAIL = "Git email must not be empty"
    INVALID_GIT_EMAIL = "Invalid git email format"
