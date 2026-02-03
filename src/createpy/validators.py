import re

from src.createpy.errors import ErrorReason

# Matches valid names that:
# - Must start with a letter
# - Can contain letters, numbers, dots, hyphens and underscores
NAME_REGEX = re.compile(r"^[a-zA-Z][\w.-]*$")

# Matches common git repo URL formats:
# - HTTPS: https://github.com/user/repo.git
# - SSH: git@github.com:user/repo.git
# - Git: git://github.com/user/repo.git
# Regex breakdown:
# ^(https:\/\/|git@|git:\/\/) - Must start with https://, git@ or git://
# [\w\d\-_\.]+ - Domain name with letters, numbers, hyphens, underscores, dots
# [:|\/] - Separator can be : (SSH) or / (HTTPS/Git)
# [\w\d\-_\/]+ - Repository path with letters, numbers, hyphens, underscores, slashes
# \.git$ - Must end with .git
REPO_REGEX = re.compile(
    r"^(https:\/\/|git@|git:\/\/)[\w\d\-_\.]+[:|\/][\w\d\-_\/]+\.git$"
)

# Matches valid git usernames:
# - Must start with a letter or number
# - Can contain letters, numbers, hyphens, underscores
# - Cannot have consecutive hyphens/underscores
# - Cannot end with hyphen/underscore
# - Length between 1-39 chars (GitHub limit)
# Regex breakdown:
# ^[a-zA-Z0-9] - Start with letter/number
# [a-zA-Z0-9-_]* - Optional middle chars
# [a-zA-Z0-9]$ - End with letter/number
# |^[a-zA-Z0-9]$ - OR single letter/number
GIT_USER_REGEX = re.compile(r"^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$|^[a-zA-Z0-9]$")

# Matches valid email formats:
# - Local part can contain letters, numbers, and .-_
# - Domain part must contain at least one dot
# - TLD must be at least 2 chars
# - Overall length must be <= 254 chars (RFC 5321)
# Regex breakdown:
# ^[a-zA-Z0-9._%+-]+ - Local part with allowed chars
# @ - Required @ symbol
# [a-zA-Z0-9.-]+ - Domain with letters, numbers, dots, hyphens
# \. - Required dot before TLD
# [a-zA-Z]{2,}$ - TLD with 2+ letters
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def validate_name(name: str | None) -> None:
    if name is None:
        return

    if not name.strip():
        raise ValueError(ErrorReason.EMPTY_NAME)
    if not NAME_REGEX.match(name):
        raise ValueError(ErrorReason.INVALID_NAME_CHARS)


def validate_repo(repo: str | None) -> None:
    if repo is None:
        return

    if not repo.strip():
        raise ValueError(ErrorReason.EMPTY_REPO)
    if not REPO_REGEX.match(repo):
        raise ValueError(ErrorReason.INVALID_REPO_URL)


def validate_git_user(git_user: str | None) -> None:
    if git_user is None:
        return

    if not git_user.strip():
        raise ValueError(ErrorReason.EMPTY_GIT_USER)
    if len(git_user) > 39:
        raise ValueError(ErrorReason.GIT_USER_TOO_LONG)
    if not GIT_USER_REGEX.match(git_user):
        raise ValueError(ErrorReason.INVALID_GIT_USER)


def validate_git_email(git_email: str | None) -> None:
    if git_email is None:
        return

    if not git_email.strip():
        raise ValueError(ErrorReason.EMPTY_GIT_EMAIL)
    if len(git_email) > 254 or not EMAIL_REGEX.match(git_email):
        raise ValueError(ErrorReason.INVALID_GIT_EMAIL)
