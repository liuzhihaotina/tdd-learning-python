import pytest

from tdd_learning_python.chapter1 import is_free_shipping, shipping_message


@pytest.mark.parametrize(
    ("order_amount", "expected"),
    [
        (0, False),
        (99, False),
        (100, True),
        (101, True),
    ],
)
def test_is_free_shipping(order_amount: int, expected: bool) -> None:
    assert is_free_shipping(order_amount) is expected


def test_is_free_shipping_rejects_negative_amount() -> None:
    with pytest.raises(ValueError, match="order_amount 不能为负数"):
        is_free_shipping(-1)


def test_shipping_message() -> None:
    assert shipping_message(100) == "订单满 100 元，免运费"
    assert shipping_message(99) == "订单未满 100 元，需支付运费"
