from tdd_learning_python.chapter5_cart import OrderSummary
from tdd_learning_python.chapter5_renderer import render_order_summary


def test_render_order_summary_with_coupon() -> None:
    summary = OrderSummary(
        subtotal=30,
        discount=10,
        total=20,
        coupon_code="SAVE10",
        coupon_description="立减 10 元",
    )

    assert render_order_summary(summary) == [
        "订单摘要：",
        "小计：30",
        "优惠：-10",
        "优惠码：SAVE10（立减 10 元）",
        "总价：20",
    ]
