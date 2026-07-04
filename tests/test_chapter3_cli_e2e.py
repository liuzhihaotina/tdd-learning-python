import subprocess
import sys


def test_chapter3_cli_e2e_password_passes() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter3_cli"],
        input="abc12345\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "请输入密码：" in result.stdout
    assert "密码校验通过" in result.stdout
    assert result.stderr == ""


def test_chapter3_cli_e2e_password_fails() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter3_cli"],
        input="ab12\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "密码校验失败" in result.stdout
    assert "密码长度至少 8 位" in result.stdout
    assert result.stderr == ""
