import pytest
from src.createpy.validators import validate_name, validate_repo, validate_git_user, validate_git_email
from src.createpy.errors import ErrorReason


class TestValidateName:
    @pytest.mark.parametrize(
        "name",
        [
            "valid_name",
            "ValidName",
            "name123",
            "name.with.dots",
            "name-with-hyphens",
            "a",
            "A1",
        ],
    )
    def test_valid_names(self, name: str):
        validate_name(name)  # Should not raise

    @pytest.mark.parametrize(
        "name,expected_error",
        [
            (None, ErrorReason.EMPTY_NAME),
            ("", ErrorReason.EMPTY_NAME),
            ("   ", ErrorReason.EMPTY_NAME),
            ("123invalid", ErrorReason.INVALID_NAME_CHARS),
            ("-invalid", ErrorReason.INVALID_NAME_CHARS),
            (".invalid", ErrorReason.INVALID_NAME_CHARS),
            ("invalid space", ErrorReason.INVALID_NAME_CHARS),
            ("invalid@char", ErrorReason.INVALID_NAME_CHARS),
        ],
    )
    def test_invalid_names(self, name: str | None, expected_error: ErrorReason):
        with pytest.raises(ValueError, match=str(expected_error)):
            validate_name(name)


class TestValidateRepo:
    @pytest.mark.parametrize(
        "repo",
        [
            "https://github.com/user/repo.git",
            "git@github.com:user/repo.git",
            "git://github.com/user/repo.git",
            "https://gitlab.com/user/project.git",
            "git@bitbucket.org:user/repo.git",
        ],
    )
    def test_valid_repos(self, repo: str):
        validate_repo(repo)  # Should not raise

    @pytest.mark.parametrize(
        "repo,expected_error",
        [
            (None, ErrorReason.EMPTY_REPO),
            ("", ErrorReason.EMPTY_REPO),
            ("   ", ErrorReason.EMPTY_REPO),
            ("invalid-url", ErrorReason.INVALID_REPO_URL),
            ("https://github.com/user/repo", ErrorReason.INVALID_REPO_URL),
            ("ftp://github.com/user/repo.git", ErrorReason.INVALID_REPO_URL),
            ("github.com/user/repo.git", ErrorReason.INVALID_REPO_URL),
        ],
    )
    def test_invalid_repos(self, repo: str | None, expected_error: ErrorReason):
        with pytest.raises(ValueError, match=str(expected_error)):
            validate_repo(repo)


class TestValidateGitUser:
    @pytest.mark.parametrize(
        "git_user",
        [
            "user",
            "user123",
            "user-name",
            "user_name",
            "a",
            "1",
            "user-123_test",
        ],
    )
    def test_valid_git_users(self, git_user: str):
        validate_git_user(git_user)  # Should not raise

    @pytest.mark.parametrize(
        "git_user,expected_error",
        [
            (None, ErrorReason.EMPTY_GIT_USER),
            ("", ErrorReason.EMPTY_GIT_USER),
            ("   ", ErrorReason.EMPTY_GIT_USER),
            ("a" * 40, ErrorReason.GIT_USER_TOO_LONG),
            ("-invalid", ErrorReason.INVALID_GIT_USER),
            ("invalid-", ErrorReason.INVALID_GIT_USER),
            ("_invalid", ErrorReason.INVALID_GIT_USER),
            ("invalid_", ErrorReason.INVALID_GIT_USER),
            ("user--name", ErrorReason.INVALID_GIT_USER),
            ("user__name", ErrorReason.INVALID_GIT_USER),
        ],
    )
    def test_invalid_git_users(self, git_user: str | None, expected_error: ErrorReason):
        with pytest.raises(ValueError, match=str(expected_error)):
            validate_git_user(git_user)


class TestValidateGitEmail:
    @pytest.mark.parametrize(
        "git_email",
        [
            "user@example.com",
            "test.email@domain.org",
            "user+tag@example.co.uk",
            "123@test.io",
            "user_name@sub.domain.com",
        ],
    )
    def test_valid_git_emails(self, git_email: str):
        validate_git_email(git_email)  # Should not raise

    @pytest.mark.parametrize(
        "git_email,expected_error",
        [
            (None, ErrorReason.EMPTY_GIT_EMAIL),
            ("", ErrorReason.EMPTY_GIT_EMAIL),
            ("   ", ErrorReason.EMPTY_GIT_EMAIL),
            ("a" * 255 + "@example.com", ErrorReason.INVALID_GIT_EMAIL),
            ("invalid-email", ErrorReason.INVALID_GIT_EMAIL),
            ("@example.com", ErrorReason.INVALID_GIT_EMAIL),
            ("user@", ErrorReason.INVALID_GIT_EMAIL),
            ("user@domain", ErrorReason.INVALID_GIT_EMAIL),
            ("user@domain.c", ErrorReason.INVALID_GIT_EMAIL),
        ],
    )
    def test_invalid_git_emails(self, git_email: str | None, expected_error: ErrorReason):
        with pytest.raises(ValueError, match=str(expected_error)):
            validate_git_email(git_email)

