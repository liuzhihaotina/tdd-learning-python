import pytest

from tdd_learning_python.chapter6 import Item, Order, PricingEngine, Receipt


@pytest.fixture
def engine() -> PricingEngine:
    return PricingEngine()


@pytest.fixture
def order_factory():
    def make_order(prices: list[int], tier: str = "basic") -> Order:
        items = [Item(name=f"Item-{index + 1}", price=price) for index, price in enumerate(prices)]
        return Order(items=items, customer_tier=tier)

    return make_order


@pytest.fixture
def pricing_scenarios(order_factory):
    return [
        {
            "name": "basic_small_order",
            "order": order_factory([10], tier="basic"),
            "expected": Receipt(
                subtotal=10,
                membership_discount=0,
                shipping_fee=12,
                tax=1,
                total=23,
                customer_tier="basic",
            ),
        },
        {
            "name": "silver_free_shipping",
            "order": order_factory([40, 60], tier="silver"),
            "expected": Receipt(
                subtotal=100,
                membership_discount=5,
                shipping_fee=0,
                tax=7,
                total=102,
                customer_tier="silver",
            ),
        },
        {
            "name": "gold_large_order",
            "order": order_factory([50, 60], tier="gold"),
            "expected": Receipt(
                subtotal=110,
                membership_discount=11,
                shipping_fee=0,
                tax=7,
                total=106,
                customer_tier="gold",
            ),
        },
    ]


def test_item_rejects_negative_price() -> None:
    with pytest.raises(ValueError, match="商品价格不能为负数"):
        Item(name="Apple", price=-1)


@pytest.mark.parametrize(
    ("tier", "expected_discount_rate"),
    [
        ("basic", 0),
        ("silver", 5),
        ("gold", 10),
    ],
)
def test_membership_discount_rates(engine: PricingEngine, order_factory, tier: str, expected_discount_rate: int) -> None:
    receipt = engine.calculate(order_factory([100], tier=tier))

    assert receipt.membership_discount == 100 * expected_discount_rate // 100


@pytest.mark.parametrize(
    ("prices", "expected_shipping_fee"),
    [
        ([40, 50], 12),
        ([60, 50], 0),
        ([100], 0),
    ],
)
def test_shipping_fee_threshold(engine: PricingEngine, order_factory, prices: list[int], expected_shipping_fee: int) -> None:
    receipt = engine.calculate(order_factory(prices))

    assert receipt.shipping_fee == expected_shipping_fee


@pytest.mark.parametrize("scenario", ["basic_small_order", "silver_free_shipping", "gold_large_order"])
def test_calculate_receipt_with_named_scenarios(engine: PricingEngine, pricing_scenarios, scenario: str) -> None:
    case = next(item for item in pricing_scenarios if item["name"] == scenario)

    receipt = engine.calculate(case["order"])

    assert receipt == case["expected"]


def test_calculate_rejects_unknown_tier(engine: PricingEngine, order_factory) -> None:
    with pytest.raises(ValueError, match="不支持的用户等级：vip"):
        engine.calculate(order_factory([10], tier="vip"))


@pytest.mark.parametrize(
    "prices, expected_total",
    [
        ([10], 23),
        ([50, 60], 118),
        ([100], 108),
    ],
)
def test_total_changes_with_item_factory(engine: PricingEngine, order_factory, prices: list[int], expected_total: int) -> None:
    receipt = engine.calculate(order_factory(prices))

    assert receipt.total == expected_total
