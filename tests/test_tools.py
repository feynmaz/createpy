import pytest
from src.createpy.tools import validate_name
from src.createpy.errors import ErrorReason


@pytest.mark.parametrize(
    "name,err",
    [
        ("validname", None),
        ("", ErrorReason.EMPTY_NAME.value),
        (" invalid chars!", ErrorReason.INVALID_NAME_CHARS.value),
    ],
)
def test_validate_name(name: str, err: str | None):
    if err:
        with pytest.raises(ValueError) as exc:
            validate_name(name)
        assert str(exc.value) == err
    else:
        # no raise
        validate_name(name)
