"""第一章：为什么需要测试

这里用“满 100 元免运费”作为示例，演示为什么需要测试来保护边界条件。
"""

from __future__ import annotations

FREE_SHIPPING_THRESHOLD = 100


def is_free_shipping(order_amount: int, threshold: int = FREE_SHIPPING_THRESHOLD) -> bool:
    """判断订单是否满足免运费条件。

    规则：当订单金额大于等于阈值时，免运费。

    Args:
        order_amount: 订单金额，必须是非负整数。
        threshold: 免运费门槛，默认 100 元。

    Returns:
        满足免运费条件返回 True，否则返回 False。

    Raises:
        ValueError: 当订单金额为负数时抛出。
    """

    if order_amount < 0:
        raise ValueError("order_amount 不能为负数")

    return order_amount >= threshold


def shipping_message(order_amount: int, threshold: int = FREE_SHIPPING_THRESHOLD) -> str:
    """生成运费提示文案。"""

    if is_free_shipping(order_amount, threshold):
        return f"订单满 {threshold} 元，免运费"
    return f"订单未满 {threshold} 元，需支付运费"
