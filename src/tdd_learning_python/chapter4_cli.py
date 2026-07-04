"""第四章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter4_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter4 import BankAccount


def main() -> int:
    """读取用户输入的菜单编号，并展示账户状态变化。"""

    account = BankAccount()
    print(f"当前余额：{account.balance}")

    while True:
        print("请选择操作：")
        print("1. 存款")
        print("2. 取款")
        print("3. 查看余额")
        print("4. 退出")

        choice = input("请输入编号：").strip()

        if choice == "4":
            print("已退出")
            return 0

        if choice == "3":
            print(f"当前余额：{account.balance}")
            continue

        if choice not in {"1", "2"}:
            print("不支持的操作")
            return 1

        amount_text = input("请输入金额：").strip()

        try:
            amount = int(amount_text)
        except ValueError:
            print("请输入有效的整数金额")
            return 1

        try:
            if choice == "1":
                account.deposit(amount)
            else:
                account.withdraw(amount)
        except ValueError as exc:
            print(str(exc))
            return 1

        print(f"当前余额：{account.balance}")


if __name__ == "__main__":
    sys.exit(main())
