# tdd-learning-python

一个面向 Python 初学测试、重点学习 **测试驱动开发（TDD）** 的教程 + 练习仓库。

## 适合谁

- 已经会写 Python，但还没系统接触过测试
- 最近 bug 较多，想通过测试提升代码质量
- 想学习如何用 TDD 提高开发效率、降低回归风险

## 推荐依赖管理工具

本仓库推荐使用 **uv**：

- 安装快，命令简单
- 适合学习项目和日常开发
- 和 `pyproject.toml` 配合自然
- 适合把“环境准备”这件事变得尽量少出错

如果你更习惯 `pip` / `venv` 也可以替换，但后续文档默认按 `uv` 编写。

## uv 与 pytest 配置说明

### 1. 安装 uv

如果你的机器还没有 `uv`，可以使用官方安装方式：

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

激活 PATH

```bash
source $HOME/.local/bin/env
```

安装完成后，重新打开终端，确认命令可用：

```bash
uv --version
```

### 2. 同步项目依赖

本项目把开发依赖写在 `pyproject.toml` 里，主要包括：

- 构建信息：`[build-system]`
- 项目信息：`[project]`
- 开发依赖：`[project.optional-dependencies].dev`
- pytest 配置：`[tool.pytest.ini_options]`

安装开发依赖时，执行：

```bash
uv sync --extra dev
```

这条命令会创建/更新虚拟环境，并安装 `pytest`。

### 3. 运行测试

安装完成后，直接运行：

```bash
uv run pytest
```

如果你只想看更详细一点的输出，可以运行：

```bash
uv run pytest -vv
```

### 4. 当前项目里的 pytest 默认配置

`pyproject.toml` 中已经为 pytest 配好了这几个默认项：

- `testpaths = ["tests"]`：只从 `tests/` 目录收集测试
- `pythonpath = ["src"]`：允许直接导入 `src/` 下的包
- `addopts = "-q"`：默认使用安静模式输出

也就是说，你以后只要把测试文件放进 `tests/`，并按正常命名写测试函数，pytest 就能找到它们。

### 5. 如果暂时不用 uv

你也可以用传统方式：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest
```

## 快速开始

先同步依赖：

```bash
uv sync --extra dev
```

然后按下面两种方式之一运行项目：

### 方式 1：推荐，使用 uv 运行项目内的 Python

```bash
uv run python -m tdd_learning_python.chapter1_cli
```

### 方式 2：直接使用虚拟环境里的 Python

```bash
./.venv/bin/python -m tdd_learning_python.chapter1_cli
```

> 注意：不要直接执行系统里的 `python` 或 `python3`，它们可能不会加载本项目的虚拟环境，因此会找不到 `tdd_learning_python`。


## 学习目标

1. 理解为什么测试能降低 bug 率
2. 掌握 TDD 的基本循环：**红 -> 绿 -> 重构**
3. 学会从最小场景开始写测试
4. 学会用测试驱动重构，避免“改一处坏一片”
5. 学会在工程实践中平衡单元测试、集成测试与可维护性

## 仓库结构

```text
.
├── docs/                 # 学习路线与章节说明
├── exercises/            # 每章练习题
├── src/tdd_learning_python/
│   └── ...               # 教学示例代码
└── tests/                # 基础验证与示例测试
```

## 学习路线

- [第一章：为什么需要测试](docs/learning-path.md#第一章为什么需要测试)
  - [第一章实战示例：为什么需要测试](docs/chapter-1-example.md)
- [第二章：TDD 基本流程](docs/learning-path.md#第二章tdd-基本流程)
  - [第二章实战示例：TDD 基本流程](docs/chapter-2-example.md)
  - [第二章 CLI + E2E 示例](docs/chapter-2-cli-e2e.md)

- [第三章：从函数开始写测试](docs/learning-path.md#第三章从函数开始写测试)
  - [第三章实战示例：从函数开始写测试](docs/chapter-3-example.md)
  - [第三章 CLI + E2E 示例](docs/chapter-3-cli-e2e.md)

- [第四章：从类与对象开始写测试](docs/learning-path.md#第四章从类与对象开始写测试)
  - [第四章实战示例：从类与对象开始写测试](docs/chapter-4-example.md)
  - [第四章 CLI + E2E 示例](docs/chapter-4-cli-e2e.md)
    - 该 CLI 采用编号菜单，可输入 `4` 主动退出


- [第五章：Mock、边界条件与重构](docs/learning-path.md#第五章mock边界条件与重构)
  - [第五章实战示例：Mock、边界条件与重构](docs/chapter-5-example.md)
  - [第五章 CLI + E2E 示例](docs/chapter-5-cli-e2e.md)


## 练习入口

- [练习 01：Hello TDD](exercises/01-hello-tdd/README.md)
- [练习 02：FizzBuzz](exercises/02-fizzbuzz/README.md)
- [练习 03：密码校验器](exercises/03-password-validator/README.md)
- [练习 04：银行账户](exercises/04-bank-account/README.md)
- [练习 05：购物车](exercises/05-shopping-cart/README.md)
- [第一章实战示例：为什么需要测试](docs/chapter-1-example.md)
- [第一章 CLI + E2E 示例](docs/chapter-1-cli-e2e.md)

## 学习建议

- 先看一章，再做一章对应练习
- 每个练习都先写测试，再写实现
- 不要追求一开始就写得“优雅”，先让测试推动你前进
- 如果卡住，先把问题缩小到“最小可验证场景”

## 常见问题

### 1. 为什么我输入 `python` 报错，但 `python3` 可以？

有些系统只把 Python 3 安装成 `python3`，没有额外提供 `python` 这个别名。学习本仓库时，优先使用 `python3`，或者使用 `uv` 来统一管理环境。

### 2. `uv` 安装后为什么终端还是找不到？

通常是因为安装完成后没有重新打开终端，或者 `uv` 的安装路径还没有加入 `PATH`。先关闭并重新打开终端，再执行：

```bash
uv --version
```

### 3. `pytest` 为什么不用单独安装？

在本仓库里，`pytest` 被放进了项目的开发依赖中。只要运行：

```bash
uv sync --extra dev
```

`pytest` 就会被安装到对应环境里，然后你可以通过：

```bash
uv run pytest
```

来执行测试。

### 4. 我可以直接用 `pip install pytest` 吗？

可以，但不推荐作为默认方式。这个项目希望你练习工程化做法，所以优先使用 `pyproject.toml` + `uv` 管理依赖，能减少环境漂移。

