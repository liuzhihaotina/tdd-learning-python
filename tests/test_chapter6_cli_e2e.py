import subprocess
import sys


def test_chapter6_cli_e2e_gold_tier() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter6_cli"],
        input="Apple\n50\nBanana\n60\n\ngold\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert "订单摘要：" in result.stdout
    assert "商品数量：2" in result.stdout
    assert "小计：110" in result.stdout
    assert "会员折扣：-11" in result.stdout
    assert "运费：0" in result.stdout
    assert "税费：7" in result.stdout
    assert "总价：106" in result.stdout
    assert result.stderr == ""


def test_chapter6_cli_rejects_unknown_tier() -> None:
    result = subprocess.run(
        [sys.executable, "-m", "tdd_learning_python.chapter6_cli"],
        input="Apple\n10\n\nvip\n",
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 1
    assert "不支持的用户等级：vip" in result.stdout
    assert result.stderr == ""
