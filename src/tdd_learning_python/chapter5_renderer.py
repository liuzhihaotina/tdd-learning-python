"""第五章：订单摘要渲染器。

把摘要对象转换成可直接输出的文本行。
"""

from __future__ import annotations

from tdd_learning_python.chapter5_cart import OrderSummary


def render_order_summary(summary: OrderSummary) -> list[str]:
    discount_text = f"-{summary.discount}" if summary.discount else "0"
    lines = [
        "订单摘要：",
        f"小计：{summary.subtotal}",
        f"优惠：{discount_text}",
    ]
    if summary.coupon_code:
        lines.append(f"优惠码：{summary.coupon_code}（{summary.coupon_description}）")
    else:
        lines.append("优惠码：未使用")
    lines.append(f"总价：{summary.total}")
    return lines

