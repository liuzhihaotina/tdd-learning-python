"""第六章：测试架构、fixture 与测试数据工厂。

这里用订单定价引擎作为示例，演示如何组织较大的测试集。
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


@dataclass(frozen=True)
class Order:
    items: list[Item] = field(default_factory=list)
    customer_tier: str = "basic"

    def subtotal(self) -> int:
        return sum(item.price for item in self.items)


@dataclass(frozen=True)
class Receipt:
    subtotal: int
    membership_discount: int
    shipping_fee: int
    tax: int
    total: int
    customer_tier: str


class PricingEngine:
    discount_rates = {
        "basic": 0,
        "silver": 5,
        "gold": 10,
    }
    free_shipping_threshold = 100
    shipping_fee_amount = 12
    tax_rate = 8

    def calculate(self, order: Order) -> Receipt:
        subtotal = order.subtotal()
        if order.customer_tier not in self.discount_rates:
            raise ValueError(f"不支持的用户等级：{order.customer_tier}")

        membership_discount = subtotal * self.discount_rates[order.customer_tier] // 100
        shipping_fee = 0 if subtotal >= self.free_shipping_threshold else self.shipping_fee_amount
        taxable_base = subtotal - membership_discount + shipping_fee
        tax = taxable_base * self.tax_rate // 100
        total = taxable_base + tax

        return Receipt(
            subtotal=subtotal,
            membership_discount=membership_discount,
            shipping_fee=shipping_fee,
            tax=tax,
            total=total,
            customer_tier=order.customer_tier,
        )
