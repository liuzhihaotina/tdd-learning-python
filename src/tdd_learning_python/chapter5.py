"""第五章兼容导出层。

历史入口，统一导出第五章拆分后的模块符号。
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
