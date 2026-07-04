"""第四章：从类与对象开始写测试

这里用银行账户作为示例，演示如何测试有状态对象。
"""

from __future__ import annotations


class BankAccount:
    """一个最小银行账户示例。"""

    def __init__(self, balance: int = 0) -> None:
        if balance < 0:
            raise ValueError("初始余额不能为负数")
        self._balance = balance

    @property
    def balance(self) -> int:
        return self._balance

    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("存款金额必须大于 0")
        self._balance += amount

    def withdraw(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("取款金额必须大于 0")
        if amount > self._balance:
            raise ValueError("余额不足")
        self._balance -= amount
