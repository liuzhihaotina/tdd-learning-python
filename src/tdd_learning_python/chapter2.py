"""第二章：TDD 基本流程

这里用 FizzBuzz 作为示例，演示如何按红 -> 绿 -> 重构一步一步推进。
"""

from __future__ import annotations


def fizzbuzz(number: int) -> int | str:
    """返回 FizzBuzz 结果。

    规则：
    - 3 的倍数返回 "Fizz"
    - 5 的倍数返回 "Buzz"
    - 3 和 5 的公倍数返回 "FizzBuzz"
    - 其他数字返回数字本身
    """

    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return number
