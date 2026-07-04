import subprocess
import sys


def test_chapter2_cli_e2e_fizzbuzz() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter2_cli"],
        input="15\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "请输入一个数字：" in result.stdout
    assert "FizzBuzz" in result.stdout
    assert result.stderr == ""


def test_chapter2_cli_e2e_rejects_invalid_number() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter2_cli"],
        input="abc\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "请输入有效的整数" in result.stdout
    assert result.stderr == ""
