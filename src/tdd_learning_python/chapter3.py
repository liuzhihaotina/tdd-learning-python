"""第三章：从函数开始写测试

这里用密码校验器作为示例，演示如何从最容易测试的纯函数开始。
"""

from __future__ import annotations

import re

MIN_PASSWORD_LENGTH = 8


def validate_password(password: str) -> tuple[bool, list[str]]:
    """校验密码是否符合基础要求。

    规则：
    - 长度至少 8 位
    - 必须包含字母
    - 必须包含数字
    - 不能包含空格

    Returns:
        (是否通过, 错误列表)
    """

    errors: list[str] = []

    if len(password) < MIN_PASSWORD_LENGTH:
        errors.append("密码长度至少 8 位")
    if not re.search(r"[A-Za-z]", password):
        errors.append("密码必须包含字母")
    if not re.search(r"\d", password):
        errors.append("密码必须包含数字")
    if " " in password:
        errors.append("密码不能包含空格")

    return len(errors) == 0, errors
