# 第三章 CLI + E2E 示例

这一节在“密码校验器”的函数测试基础上，再加一层**用户交互入口**，演示端到端测试如何覆盖完整用户流程。

---

## 为什么需要 CLI

密码校验器本身是纯函数，但真实项目里，用户通常不是直接调用函数，而是通过：

- 命令行
- 表单
- 接口
- 其他系统调用

CLI 是最简单的用户入口，因此很适合拿来演示 E2E。

---

## 本示例做了什么

用户输入：

```text
abc12345
```

程序输出：

```text
请输入密码：密码校验通过
```

如果输入：

```text
ab12
```

程序输出：

```text
密码校验失败
- 密码长度至少 8 位
```

---

## 代码位置

- CLI 入口：`src/tdd_learning_python/chapter3_cli.py`
- E2E 测试：`tests/test_chapter3_cli_e2e.py`

---

## 如何运行

先确保依赖已经同步：

```bash
uv sync --extra dev
```

然后按下面两种方式之一运行：

### 方式 1：推荐，使用 uv

```bash
uv run python -m tdd_learning_python.chapter3_cli
```

### 方式 2：直接使用虚拟环境里的 Python

```bash
./.venv/bin/python -m tdd_learning_python.chapter3_cli
```

然后输入一个密码，例如：

```text
abc12345
```

---

## 如何测试

端到端测试会真正启动一个独立进程，向它输入内容，再检查输出结果：

```bash
./.venv/bin/pytest tests/test_chapter3_cli_e2e.py -q
```

---

## 你应该观察什么

- 输入 `abc12345` 时，程序返回“密码校验通过”
- 输入 `ab12` 时，程序返回失败提示和错误列表
- 这个测试覆盖的是“用户怎么使用这个程序”，不是内部函数实现细节

这就是 E2E 的价值：它能帮你确认**从入口到结果**这条链路是通的。
