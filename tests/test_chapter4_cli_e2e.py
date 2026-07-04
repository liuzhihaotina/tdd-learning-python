import subprocess
import sys


def test_chapter4_cli_e2e_deposit_then_balance_then_exit() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter4_cli"],
        input="deposit\n50\nbalance\nexit\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "当前余额：0" in result.stdout
    assert "当前余额：50" in result.stdout
    assert result.stdout.rstrip().endswith("已退出")
    assert result.stderr == ""


def test_chapter4_cli_e2e_withdraw_too_much() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter4_cli"],
        input="withdraw\n50\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "余额不足" in result.stdout
    assert result.stderr == ""
