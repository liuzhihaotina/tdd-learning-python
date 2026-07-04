"""第五章：购物车模块。

这里放购物车和订单摘要，保持尽量纯粹，便于测试。
"""

from __future__ import annotations

from dataclasses import dataclass, field

from tdd_learning_python.chapter5_coupon import CouponService, Item


@dataclass(frozen=True)
class OrderSummary:
    subtotal: int
    discount: int
    total: int
    coupon_code: str | None = None
    coupon_description: str | None = None


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def subtotal(self) -> int:
        return sum(item.price for item in self.items)

    def summary(self, coupon_code: str | None = None, coupon_service: CouponService | None = None) -> OrderSummary:
        subtotal = self.subtotal()
        if not coupon_code:
            return OrderSummary(subtotal=subtotal, discount=0, total=subtotal)
        if coupon_service is None:
            raise ValueError("使用优惠码时必须提供 coupon_service")

        discount = coupon_service.get_discount(coupon_code, subtotal)
        if discount < 0:
            raise ValueError("折扣不能为负数")
        if discount > subtotal:
            raise ValueError("折扣不能超过小计")

        description = coupon_service.describe(coupon_code)
        return OrderSummary(
            subtotal=subtotal,
            discount=discount,
            total=subtotal - discount,
            coupon_code=coupon_code,
            coupon_description=description,
        )

    def total(self, coupon_code: str | None = None, coupon_service: CouponService | None = None) -> int:
        return self.summary(coupon_code=coupon_code, coupon_service=coupon_service).total
