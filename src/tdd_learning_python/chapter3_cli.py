"""第三章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter3_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter3 import validate_password


def main() -> int:
    """读取用户输入的密码，并输出校验结果。"""

    password = input("请输入密码：").strip()
    valid, errors = validate_password(password)

    if valid:
        print("密码校验通过")
        return 0

    print("密码校验失败")
    for error in errors:
        print(f"- {error}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
