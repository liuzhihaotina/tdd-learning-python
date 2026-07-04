import pytest

from tdd_learning_python.chapter3 import validate_password


@pytest.mark.parametrize(
    ("password", "expected_valid", "expected_errors"),
    [
        ("abc12345", True, []),
        ("abcdefg", False, ["密码长度至少 8 位", "密码必须包含数字"]),
        ("12345678", False, ["密码必须包含字母"]),
        ("abcd ef12", False, ["密码不能包含空格"]),
        ("ab12", False, ["密码长度至少 8 位"]),
    ],
)
def test_validate_password(password: str, expected_valid: bool, expected_errors: list[str]) -> None:
    valid, errors = validate_password(password)

    assert valid is expected_valid
    assert errors == expected_errors
