# 第五章 CLI + E2E 示例

这一节在“购物车 + 折扣码服务”的基础上，再加一层**用户交互入口**，演示如何通过 E2E 覆盖外部依赖与边界条件。

---

## 为什么需要 CLI

当系统开始涉及多个对象协作和外部依赖时，CLI 可以帮助你模拟一条完整的用户路径：

- 录入商品
- 查看可用优惠码
- 输入优惠码
- 查看小计、优惠和总价摘要

---

## 本示例做了什么

用户输入：

```text
Apple
10
Banana
20

SAVE10
```

程序输出：

```text
订单摘要：
小计：30
优惠：-10
优惠码：SAVE10（立减 10 元）
总价：20
```

如果输入：

```text
Apple
10

list
NOPE
HALF
```

程序会先列出可用优惠码，然后在输入无效优惠码时给出更友好的提示，直到输入有效优惠码或直接回车跳过。

如果输入：

```text
Apple
abc
```

程序输出：

```text
请输入有效的整数价格
```

---

## 代码位置

- CLI 入口：`src/tdd_learning_python/chapter5_cli.py`
- E2E 测试：`tests/test_chapter5_cli_e2e.py`
- 兼容导出层：`src/tdd_learning_python/chapter5.py`

---

## 如何运行

先确保依赖已经同步：

```bash
uv sync --extra dev
```

然后按下面两种方式之一运行：

### 方式 1：推荐，使用 uv

```bash
uv run python -m tdd_learning_python.chapter5_cli
```

### 方式 2：直接使用虚拟环境里的 Python

```bash
./.venv/bin/python -m tdd_learning_python.chapter5_cli
```

---

## 如何测试

端到端测试会真正启动一个独立进程，向它输入内容，再检查输出结果：

```bash
./.venv/bin/pytest tests/test_chapter5_cli_e2e.py -q
```

---

## 你应该观察什么

- 小计、优惠和总价是否正确
- 是否能查看可用优惠码
- 无效优惠码是否给出友好提示并重新输入
- 非法价格是否被拒绝
- 这个测试覆盖的是“用户怎么录入商品并使用优惠码”，不是内部实现细节

这就是 E2E 的价值：它能帮你确认**从入口到结果**这条链路是通的。
