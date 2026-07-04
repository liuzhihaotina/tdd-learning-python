import pytest

from tdd_learning_python.chapter5 import CouponService, Item, ShoppingCart


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


def test_total_uses_coupon_service_mock() -> None:
    class FakeCouponService(CouponService):
        def get_discount(self, code: str, subtotal: int) -> int:
            assert code == "SAVE10"
            assert subtotal == 100
            return 10

    cart = ShoppingCart([Item(name="Apple", price=40), Item(name="Banana", price=60)])

    assert cart.total(coupon_code="SAVE10", coupon_service=FakeCouponService()) == 90


def test_total_requires_coupon_service_when_coupon_code_is_used() -> None:
    cart = ShoppingCart([Item(name="Apple", price=40)])

    with pytest.raises(ValueError, match="必须提供 coupon_service"):
        cart.total(coupon_code="SAVE10")


def test_total_rejects_too_large_discount() -> None:
    class FakeCouponService(CouponService):
        def get_discount(self, code: str, subtotal: int) -> int:
            return subtotal + 1

    cart = ShoppingCart([Item(name="Apple", price=10)])

    with pytest.raises(ValueError, match="折扣不能超过小计"):
        cart.total(coupon_code="SAVE10", coupon_service=FakeCouponService())
