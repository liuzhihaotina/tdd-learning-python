"""第一章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter1_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter1 import shipping_message


def main() -> int:
    """读取用户输入的订单金额，并输出运费提示。"""

    raw_value = input("请输入订单金额：").strip()

    try:
        order_amount = int(raw_value)
    except ValueError:
        print("请输入有效的整数金额")
        return 1

    try:
        message = shipping_message(order_amount)
    except ValueError as exc:
        print(str(exc))
        return 1

    print(message)
    return 0


if __name__ == "__main__":
    sys.exit(main())
