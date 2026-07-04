"""第五章：优惠服务模块。

这里放优惠码规则、优惠服务接口和默认配置。
"""

from __future__ import annotations

from dataclasses import dataclass
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


def build_default_coupon_service() -> CouponCatalogService:
    return CouponCatalogService(
        rules={
            "SAVE10": CouponRule(description="立减 10 元", kind="fixed", value=10),
            "HALF": CouponRule(description="五折优惠", kind="percent", value=50),
            "MINUS5": CouponRule(description="立减 5 元", kind="fixed", value=5),
        }
    )
