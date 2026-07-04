"""第五章：Mock、边界条件与重构

兼容入口，向下拆分到优惠服务、购物车和订单摘要渲染器。
"""

from __future__ import annotations

from tdd_learning_python.chapter5_cart import OrderSummary, ShoppingCart
from tdd_learning_python.chapter5_coupon import (
    CouponCatalogService,
    CouponRule,
    CouponService,
    Item,
    build_default_coupon_service,
)
from tdd_learning_python.chapter5_renderer import render_order_summary

__all__ = [
    "CouponCatalogService",
    "CouponRule",
    "CouponService",
    "Item",
    "OrderSummary",
    "ShoppingCart",
    "build_default_coupon_service",
    "render_order_summary",
]
