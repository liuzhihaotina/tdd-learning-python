"""第五章：Mock、边界条件与重构

这里用购物车和可注入的优惠码服务作为示例，演示如何处理外部依赖。
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol


@dataclass(frozen=True)
class Item:
    name: str
    price: int

    def __post_init__(self) -> None:
        if self.price < 0:
            raise ValueError("商品价格不能为负数")


@dataclass(frozen=True)
class CouponRule:
    """单个优惠规则。"""

    description: str
    kind: str
    value: int

    def discount(self, subtotal: int) -> int:
        if subtotal < 0:
            raise ValueError("小计不能为负数")
        if self.kind == "fixed":
            return min(self.value, subtotal)
        if self.kind == "percent":
            return subtotal * self.value // 100
        raise ValueError(f"不支持的优惠规则类型：{self.kind}")


class CouponService(Protocol):
    """外部折扣服务的抽象。"""

    def available_codes(self) -> list[str]:
        ...

    def describe(self, code: str) -> str:
        ...

    def get_discount(self, code: str, subtotal: int) -> int:
        ...


@dataclass(frozen=True)
class CouponCatalogService:
    """基于配置的优惠码服务。"""

    rules: dict[str, CouponRule]

    def available_codes(self) -> list[str]:
        return sorted(self.rules.keys())

    def describe(self, code: str) -> str:
        rule = self.rules.get(code)
        if rule is None:
            raise ValueError(self.unknown_coupon_message(code))
        return rule.description

    def get_discount(self, code: str, subtotal: int) -> int:
        rule = self.rules.get(code)
        if rule is None:
            raise ValueError(self.unknown_coupon_message(code))
        return rule.discount(subtotal)

    def unknown_coupon_message(self, code: str) -> str:
        available = "、".join(self.available_codes()) or "无"
        return f"不支持的优惠码：{code}。可用优惠码：{available}"


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


def build_default_coupon_service() -> CouponCatalogService:
    return CouponCatalogService(
        rules={
            "SAVE10": CouponRule(description="立减 10 元", kind="fixed", value=10),
            "HALF": CouponRule(description="五折优惠", kind="percent", value=50),
            "MINUS5": CouponRule(description="立减 5 元", kind="fixed", value=5),
        }
    )
