"""第五章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter5_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter5 import Item, ShoppingCart


def main() -> int:
    """读取用户输入的商品和优惠信息，并计算购物车总价。"""

    cart = ShoppingCart()
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

    coupon_code = input("优惠码（可直接回车跳过）：").strip() or None
    subtotal = cart.subtotal()
    total = subtotal

    if coupon_code:
        if coupon_code == "SAVE10":
            total = max(0, subtotal - 10)
        else:
            print("不支持的优惠码")
            return 1

    print(f"小计：{subtotal}")
    print(f"总价：{total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
