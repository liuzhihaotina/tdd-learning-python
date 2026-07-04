# 第五章实战示例：Mock、边界条件与重构

这一章用“购物车 + 折扣码服务”来练习更接近工程实践的测试方式。

---

## 为什么这一章要学 Mock

当你的代码开始依赖外部服务、数据库、接口或第三方系统时，测试就不能只盯着纯函数了。此时常见做法是：

- 核心逻辑尽量保持纯净
- 外部依赖通过抽象或接口注入
- 测试里用 Fake / Stub / Mock 替代真实依赖

---

## 需求

- 可以加入商品
- 可以计算总价
- 可以应用优惠规则
- 可以输出订单摘要

这里我们先聚焦在“购物车金额计算 + 折扣码服务”上。

---

## 推荐的 TDD 顺序

### 1. 先写小计

```python
cart = ShoppingCart()
cart.add_item(Item(name="Apple", price=10))
assert cart.subtotal() == 10
```

### 2. 再写总价

```python
assert cart.total() == 10
```

### 3. 再引入外部折扣服务

```python
assert cart.total(coupon_code="SAVE10", coupon_service=fake_service) == 90
```

### 4. 最后补边界条件

- 商品价格不能为负数
- 折扣不能超过小计
- 使用优惠码时必须提供服务

---

## 代码位置

- 实现：`src/tdd_learning_python/chapter5.py`
- 测试：`tests/test_chapter5.py`
- CLI：`src/tdd_learning_python/chapter5_cli.py`
- E2E 测试：`tests/test_chapter5_cli_e2e.py`

---

## 你应该观察什么

- 把核心逻辑和外部依赖分开后，测试会更稳定
- Mock 不应该替代一切，只有在外部依赖存在时才有意义
- 边界条件要单独测，不要和正常逻辑混在一起

这个例子重点是让你体会：

> **先把业务核心做成可测试的小单元，再用 Mock 处理外部依赖。**

如果你想看更接近真实使用场景的版本，可以继续阅读 `docs/chapter-5-cli-e2e.md`，那里会展示如何把购物车包装成一个最小命令行程序，并用 E2E 测试模拟用户输入与优惠码选择。
