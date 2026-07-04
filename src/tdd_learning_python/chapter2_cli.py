"""第二章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter2_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter2 import fizzbuzz


def main() -> int:
    """读取用户输入的数字，并输出 FizzBuzz 结果。"""

    raw_value = input("请输入一个数字：").strip()

    try:
        number = int(raw_value)
    except ValueError:
        print("请输入有效的整数")
        return 1

    print(fizzbuzz(number))
    return 0


if __name__ == "__main__":
    sys.exit(main())
