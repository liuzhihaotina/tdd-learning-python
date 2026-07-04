import subprocess
import sys


def test_chapter5_cli_e2e_with_coupon() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter5_cli"],
        input="Apple\n10\nBanana\n20\n\nSAVE10\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "小计：30" in result.stdout
    assert "总价：20" in result.stdout
    assert result.stderr == ""


def test_chapter5_cli_e2e_rejects_invalid_price() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter5_cli"],
        input="Apple\nabc\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "请输入有效的整数价格" in result.stdout
    assert result.stderr == ""
