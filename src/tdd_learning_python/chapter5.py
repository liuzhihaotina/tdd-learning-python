"""第五章：Mock、边界条件与重构

这里用购物车和折扣码服务作为示例，演示如何处理外部依赖。
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Item:
    name: str
    price: int

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("商品价格不能为负数")


class CouponService:
    """外部折扣服务的抽象。"""

    def get_discount(self, code: str, subtotal: int) -> int:
        raise NotImplementedError


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    def subtotal(self) -> int:
        return sum(item.price for item in self.items)

    def total(self, coupon_code: str | None = None, coupon_service: CouponService | None = None) -> int:
        subtotal = self.subtotal()
        if not coupon_code:
            return subtotal
        if coupon_service is None:
            raise ValueError("使用优惠码时必须提供 coupon_service")

        discount = coupon_service.get_discount(coupon_code, subtotal)
        if discount < 0:
            raise ValueError("折扣不能为负数")
        if discount > subtotal:
            raise ValueError("折扣不能超过小计")
        return subtotal - discount
