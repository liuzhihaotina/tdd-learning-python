import subprocess
import sys


def test_chapter5_cli_e2e_with_coupon_and_summary() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter5_cli"],
        input="Apple\n10\nBanana\n20\n\nSAVE10\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "订单摘要：" in result.stdout
    assert "小计：30" in result.stdout
    assert "优惠：-10" in result.stdout
    assert "优惠码：SAVE10（立减 10 元）" in result.stdout
    assert "总价：20" in result.stdout
    assert result.stderr == ""


def test_chapter5_cli_lists_coupon_codes_and_reprompts() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter5_cli"],
        input="Apple\n10\n\nlist\nNOPE\nHALF\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "可用优惠码：" in result.stdout
    assert "- HALF: 五折优惠" in result.stdout
    assert "不支持的优惠码：NOPE。可用优惠码：HALF、MINUS5、SAVE10" in result.stdout
    assert "总价：5" in result.stdout
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
