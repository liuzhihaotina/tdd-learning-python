"""第五章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter5_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter5_cart import ShoppingCart
from tdd_learning_python.chapter5_coupon import Item, build_default_coupon_service
from tdd_learning_python.chapter5_renderer import render_order_summary


def _read_coupon_code(cart: ShoppingCart, coupon_service) -> str | None:
    while True:
        print("可用优惠码：")
        for code in coupon_service.available_codes():
            print(f"- {code}: {coupon_service.describe(code)}")
        code = input("请输入优惠码（回车跳过，输入 list 重新查看）：").strip()
        if not code:
            return None
        if code.lower() == "list":
            continue
        try:
            coupon_service.get_discount(code, cart.subtotal())
        except ValueError as exc:
            print(str(exc))
            continue
        return code


def main() -> int:
    """读取用户输入的商品和优惠信息，并输出订单摘要。"""

    cart = ShoppingCart()
    coupon_service = build_default_coupon_service()
    print("请输入商品；输入空行结束商品录入")

    while True:
        name = input("商品名称：").strip()
        if not name:
            break
        price_text = input("商品价格：").strip()
        try:
            price = int(price_text)
        except ValueError:
            print("请输入有效的整数价格")
            return 1
        try:
            cart.add_item(Item(name=name, price=price))
        except ValueError as exc:
            print(str(exc))
            return 1

    coupon_code = _read_coupon_code(cart, coupon_service)
    try:
        summary = cart.summary(coupon_code=coupon_code, coupon_service=coupon_service)
    except ValueError as exc:
        print(str(exc))
        return 1

    for line in render_order_summary(summary):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
