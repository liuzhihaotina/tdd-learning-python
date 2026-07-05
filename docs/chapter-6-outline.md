# 第六章：测试架构、fixture 与测试数据工厂

这一章进入更接近工程实践的测试组织方式：

- 如何用 `fixture` 组织测试前置条件
- 如何把重复的测试数据抽成工厂
- 如何把回归用例整理成可维护的结构
- 如何在较大的测试集合里保持可读性
- 如何让单元测试、参数化测试和 E2E 测试各司其职

---

## 目标

让你学会把“会写测试”升级成“会设计测试结构”。

---

## 你会学到

- `fixture` 的作用与边界
- `pytest.mark.parametrize` 的进阶用法
- 测试数据工厂（test data factory）的基本思路
- 如何维护回归测试集
- 如何避免测试抽象过度，保持意图清晰

---

## 章节结构

这一章建议按下面顺序学习：

1. 先看 `docs/chapter-6-example.md`
2. 再看 `docs/chapter-6-cli-e2e.md`
3. 结合 `tests/test_chapter6.py` 观察 fixture、工厂和参数化如何协作
4. 最后回到 `exercises/06-test-architecture/README.md` 完成练习

---

## 工程化检查清单

当你写第六章相关测试时，可以先检查这些问题：

- 重复的 Arrange 数据是否已经抽成 fixture 或工厂
- 同一类输入变化是否适合用参数化测试表达
- 回归用例是否使用业务化名称描述场景
- 断言是否聚焦行为，而不是内部实现细节
- 测试文件是否保持“读起来像说明书”

---

## 练习

- 阅读 `docs/chapter-6-example.md`
- 阅读 `docs/chapter-6-cli-e2e.md`
- 阅读 `exercises/06-test-architecture/README.md`
- 把重复测试数据抽成 fixture 或工厂
- 把一组相关回归用例整理成参数化测试
- 学会让测试可读、可维护、可扩展
