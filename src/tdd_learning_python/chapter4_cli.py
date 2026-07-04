"""第四章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter4_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter4 import BankAccount


def main() -> int:
    """读取用户输入的操作，并展示账户状态变化。"""

    account = BankAccount()
    print(f"当前余额：{account.balance}")

    command = input("请输入操作（deposit/withdraw）: ").strip()
    amount_text = input("请输入金额：").strip()

    try:
        amount = int(amount_text)
    except ValueError:
        print("请输入有效的整数金额")
        return 1

    try:
        if command == "deposit":
            account.deposit(amount)
        elif command == "withdraw":
            account.withdraw(amount)
        else:
            print("不支持的操作")
            return 1
    except ValueError as exc:
        print(str(exc))
        return 1

    print(f"当前余额：{account.balance}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
