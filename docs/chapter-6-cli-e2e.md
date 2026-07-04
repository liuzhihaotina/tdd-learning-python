# 第六章 CLI + E2E 示例

这一节把第六章的“测试架构”内容落到一个最小 CLI 场景里，让你看到 fixture、参数化和工厂不仅能让测试更好写，也能让完整用户流程更容易验证。

---

## 为什么需要 CLI

当系统开始涉及多个对象协作时，CLI 可以帮助你模拟一条完整的用户路径：

- 录入商品
- 选择用户等级
- 查看订单摘要

---

## 本示例做了什么

用户输入：

```text
Apple
50
Banana
60

gold
```

程序输出：

```text
订单摘要：
商品数量：2
小计：110
会员折扣：-11
运费：0
税费：7
总价：106
```

如果输入：

```text
Apple
10

vip
```

程序输出：

```text
不支持的用户等级：vip
```

---

## 代码位置

- CLI 入口：`src/tdd_learning_python/chapter6_cli.py`
- E2E 测试：`tests/test_chapter6_cli_e2e.py`
- 兼容导出层：`src/tdd_learning_python/chapter6.py`

---

## 如何运行

先确保依赖已经同步：

```bash
uv sync --extra dev
```

然后按下面两种方式之一运行：

### 方式 1：推荐，使用 uv

```bash
uv run python -m tdd_learning_python.chapter6_cli
```

### 方式 2：直接使用虚拟环境里的 Python

```bash
./.venv/bin/python -m tdd_learning_python.chapter6_cli
```

---

## 如何测试

端到端测试会真正启动一个独立进程，向它输入内容，再检查输出结果：

```bash
./.venv/bin/pytest tests/test_chapter6_cli_e2e.py -q
```

---

## 你应该观察什么

- CLI 是否能把多个商品录入成订单
- 不同等级是否会影响最终总价
- 非法等级是否会被拒绝
- 这个测试覆盖的是“用户如何使用定价引擎”，不是内部实现细节

这就是 E2E 的价值：它能帮你确认**从入口到结果**这条链路是通的。
