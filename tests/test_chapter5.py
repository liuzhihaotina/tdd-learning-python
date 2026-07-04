import pytest

from tdd_learning_python.chapter5 import (
    CouponCatalogService,
    CouponRule,
    Item,
    OrderSummary,
    ShoppingCart,
    build_default_coupon_service,
    render_order_summary,
)


def test_item_rejects_negative_price() -> None:
    with pytest.raises(ValueError, match="商品价格不能为负数"):
        Item(name="Apple", price=-1)


def test_shopping_cart_subtotal() -> None:
    cart = ShoppingCart()
    cart.add_item(Item(name="Apple", price=10))
    cart.add_item(Item(name="Banana", price=20))

    assert cart.subtotal() == 30


def test_total_without_coupon_equals_subtotal() -> None:
    cart = ShoppingCart([Item(name="Apple", price=10), Item(name="Banana", price=20)])

    assert cart.total() == 30


def test_summary_without_coupon() -> None:
    cart = ShoppingCart([Item(name="Apple", price=10), Item(name="Banana", price=20)])

    summary = cart.summary()

    assert summary.subtotal == 30
    assert summary.discount == 0
    assert summary.total == 30
    assert summary.coupon_code is None
    assert summary.coupon_description is None


def test_render_order_summary_without_coupon() -> None:
    summary = OrderSummary(subtotal=30, discount=0, total=30)

    assert render_order_summary(summary) == [
        "订单摘要：",
        "小计：30",
        "优惠：0",
        "优惠码：未使用",
        "总价：30",
    ]


def test_total_uses_coupon_service_mock() -> None:
    class FakeCouponService:
        def available_codes(self) -> list[str]:
            return ["SAVE10"]

        def describe(self, code: str) -> str:
            assert code == "SAVE10"
            return "立减 10 元"

        def get_discount(self, code: str, subtotal: int) -> int:
            assert code == "SAVE10"
            assert subtotal == 100
            return 10

    cart = ShoppingCart([Item(name="Apple", price=40), Item(name="Banana", price=60)])

    summary = cart.summary(coupon_code="SAVE10", coupon_service=FakeCouponService())

    assert summary.total == 90
    assert summary.discount == 10
    assert summary.coupon_description == "立减 10 元"


def test_total_requires_coupon_service_when_coupon_code_is_used() -> None:
    cart = ShoppingCart([Item(name="Apple", price=40)])

    with pytest.raises(ValueError, match="必须提供 coupon_service"):
        cart.summary(coupon_code="SAVE10")


def test_total_rejects_too_large_discount() -> None:
    class FakeCouponService:
        def available_codes(self) -> list[str]:
            return ["SAVE10"]

        def describe(self, code: str) -> str:
            return "立减 10 元"

        def get_discount(self, code: str, subtotal: int) -> int:
            return subtotal + 1

    cart = ShoppingCart([Item(name="Apple", price=10)])

    with pytest.raises(ValueError, match="折扣不能超过小计"):
        cart.summary(coupon_code="SAVE10", coupon_service=FakeCouponService())


def test_configured_coupon_service_supports_multiple_codes() -> None:
    service = build_default_coupon_service()

    assert service.available_codes() == ["HALF", "MINUS5", "SAVE10"]
    assert service.get_discount("SAVE10", 100) == 10
    assert service.get_discount("HALF", 100) == 50
    assert service.get_discount("MINUS5", 100) == 5


def test_configured_coupon_service_rejects_unknown_code() -> None:
    service = build_default_coupon_service()

    with pytest.raises(ValueError, match="不支持的优惠码：NOPE。可用优惠码：HALF、MINUS5、SAVE10"):
        service.get_discount("NOPE", 100)


def test_coupon_rule_percent() -> None:
    rule = CouponRule(description="五折优惠", kind="percent", value=50)

    assert rule.discount(100) == 50
