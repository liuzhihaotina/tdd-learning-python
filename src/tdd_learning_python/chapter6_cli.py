"""第六章 CLI 入口。

用法：
    python -m tdd_learning_python.chapter6_cli
"""

from __future__ import annotations

import sys

from tdd_learning_python.chapter6 import Item, Order, PricingEngine


def _read_tier() -> str:
    try:
        tier = input("请输入用户等级（basic/silver/gold）：").strip()
    except EOFError:
        return "basic"
    return tier or "basic"


def main() -> int:
    """读取商品、用户等级并输出定价结果。"""

    engine = PricingEngine()
    items: list[Item] = []
    print("请输入商品；输入空行结束商品录入")

    while True:
        try:
            name = input("商品名称：").strip()
        except EOFError:
            break
        if not name:
            break
        try:
            price_text = input("商品价格：").strip()
        except EOFError:
            print("请输入有效的整数价格")
            return 1
        try:
            price = int(price_text)
        except ValueError:
            print("请输入有效的整数价格")
            return 1
        try:
            items.append(Item(name=name, price=price))
        except ValueError as exc:
            print(str(exc))
            return 1

    tier = _read_tier()
    try:
        receipt = engine.calculate(Order(items=items, customer_tier=tier))
    except ValueError as exc:
        print(str(exc))
        return 1

    print("订单摘要：")
    print(f"商品数量：{len(items)}")
    print(f"小计：{receipt.subtotal}")
    print(f"会员折扣：-{receipt.membership_discount}")
    print(f"运费：{receipt.shipping_fee}")
    print(f"税费：{receipt.tax}")
    print(f"总价：{receipt.total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

