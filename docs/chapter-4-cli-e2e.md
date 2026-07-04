# 第四章 CLI + E2E 示例

这一节在“银行账户”的对象测试基础上，再加一层**用户交互入口**，用来演示端到端测试如何覆盖状态变化的完整流程。

---

## 为什么需要 CLI

银行账户是有状态对象，真实项目里常常不会直接调用对象方法，而是通过命令行、接口或者界面来触发操作。

CLI 是一个很适合教学的入口，因为它能直观看到：

- 初始状态
- 状态变化
- 异常分支

---

## 本示例做了什么

用户输入：

```text
deposit
50
```

程序输出：

```text
当前余额：0
当前余额：50
```

如果输入：

```text
withdraw
50
```

程序输出：

```text
余额不足
```

---

## 代码位置

- CLI 入口：`src/tdd_learning_python/chapter4_cli.py`
- E2E 测试：`tests/test_chapter4_cli_e2e.py`

---

## 如何运行

先确保依赖已经同步：

```bash
uv sync --extra dev
```

然后按下面两种方式之一运行：

### 方式 1：推荐，使用 uv

```bash
uv run python -m tdd_learning_python.chapter4_cli
```

### 方式 2：直接使用虚拟环境里的 Python

```bash
./.venv/bin/python -m tdd_learning_python.chapter4_cli
```

---

## 如何测试

端到端测试会真正启动一个独立进程，向它输入内容，再检查输出结果：

```bash
./.venv/bin/pytest tests/test_chapter4_cli_e2e.py -q
```

---

## 你应该观察什么

- 初始余额是否正确
- 存款是否改变余额
- 取款失败时是否返回错误
- 这个测试覆盖的是“用户怎么操作账户”，不是内部实现细节

这就是 E2E 的价值：它能帮你确认**从入口到结果**这条链路是通的。
