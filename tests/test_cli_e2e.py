import subprocess
import sys


def test_cli_e2e_free_shipping() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter1_cli"],
        input="100\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "请输入订单金额：" in result.stdout
    assert "订单满 100 元，免运费" in result.stdout
    assert result.stderr == ""


def test_cli_e2e_rejects_negative_amount() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter1_cli"],
        input="-1\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "order_amount 不能为负数" in result.stdout
    assert result.stderr == ""
