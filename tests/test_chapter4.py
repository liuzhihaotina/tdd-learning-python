import pytest

from tdd_learning_python.chapter4 import BankAccount


def test_initial_balance_defaults_to_zero() -> None:
    account = BankAccount()

    assert account.balance == 0


def test_initial_balance_can_be_set() -> None:
    account = BankAccount(100)

    assert account.balance == 100


def test_deposit_increases_balance() -> None:
    account = BankAccount()

    account.deposit(50)

    assert account.balance == 50


def test_withdraw_decreases_balance() -> None:
    account = BankAccount(100)

    account.withdraw(40)

    assert account.balance == 60


def test_withdraw_raises_when_balance_is_insufficient() -> None:
    account = BankAccount(10)

    with pytest.raises(ValueError, match="余额不足"):
        account.withdraw(20)


def test_rejects_negative_initial_balance() -> None:
    with pytest.raises(ValueError, match="初始余额不能为负数"):
        BankAccount(-1)
