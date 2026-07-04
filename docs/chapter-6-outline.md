# 第六章：测试架构、fixture 与测试数据工厂

这一章进入更接近工程实践的测试组织方式：

- 如何用 `fixture` 组织测试前置条件
- 如何把重复的测试数据抽成工厂
- 如何把回归用例整理成可维护的结构
- 如何在较大的测试集合里保持可读性

---

## 目标

让你学会把“会写测试”升级成“会设计测试结构”。

---

## 你会学到

- `fixture` 的作用与边界
- `pytest.mark.parametrize` 的进阶用法
- 测试数据工厂（test data factory）的基本思路
- 如何维护回归测试集

---

## 练习

- 阅读 `docs/chapter-6-example.md`
- 阅读 `docs/chapter-6-cli-e2e.md`
- 阅读 `exercises/06-test-architecture/README.md`
- 把重复测试数据抽成 fixture 或工厂
- 把一组相关回归用例整理成参数化测试
- 学会让测试可读、可维护、可扩展
