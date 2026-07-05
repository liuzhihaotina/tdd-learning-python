# 第二章 CLI + E2E 示例

这一节在 FizzBuzz 的函数测试基础上，再加一层**用户交互入口**，用来演示端到端测试。

---

## 为什么需要 CLI

FizzBuzz 本身是纯函数，但真实项目里，用户通常不是直接调用函数，而是通过：

- 命令行
- Web 表单
- 接口请求
- 后台任务

CLI 是最简单的用户入口，因此很适合拿来演示 E2E。

---

## 本示例做了什么

用户输入：

```text
15
```

程序输出：

```text
请输入一个数字：FizzBuzz
```

如果输入：

```text
abc
```

程序输出：

```text
请输入有效的整数
```

---

## 代码位置

- CLI 入口：`src/tdd_learning_python/chapter2_cli.py`
- E2E 测试：`tests/test_chapter2_cli_e2e.py`

---

## 如何运行

先确保依赖已经同步：

```bash
uv sync --extra dev
```

然后按下面两种方式之一运行：

### 方式 1：推荐，使用 uv

```bash
uv run python -m tdd_learning_python.chapter2_cli
```

### 方式 2：直接使用虚拟环境里的 Python

```bash
./.venv/bin/python -m tdd_learning_python.chapter2_cli
```

然后输入一个数字，例如：

```text
15
```

---

## 如何测试

端到端测试会真正启动一个独立进程，向它输入内容，再检查输出结果：

```bash
./.venv/bin/pytest tests/test_chapter2_cli_e2e.py -q
```

---

## 你应该观察什么

- 输入 `15` 时，程序返回 `FizzBuzz`
- 输入 `abc` 时，程序返回错误提示并以非 0 退出
- 这个测试覆盖的是“用户怎么使用这个程序”，不是内部函数实现细节

这就是 E2E 的价值：它能帮你确认**从入口到结果**这条链路是通的。
