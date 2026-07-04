# 第二章实战示例：TDD 基本流程

这一章用 FizzBuzz 来演示最经典的 TDD 循环：

1. Red：先写一个会失败的测试
2. Green：写最少代码让测试通过
3. Refactor：在测试保护下整理实现

---

## 需求

- 3 的倍数返回 `Fizz`
- 5 的倍数返回 `Buzz`
- 3 和 5 的公倍数返回 `FizzBuzz`
- 其他数字返回数字本身

---

## 为什么用 FizzBuzz

FizzBuzz 很适合入门，因为它足够简单，又能覆盖几种典型情况：

- 普通输入
- 单一规则分支
- 多规则组合
- 需要注意分支顺序

---

## 推荐的 TDD 顺序

### 1. 先写最普通的输入

```python
assert fizzbuzz(1) == 1
```

### 2. 再补 3 的倍数

```python
assert fizzbuzz(3) == "Fizz"
```

### 3. 再补 5 的倍数

```python
assert fizzbuzz(5) == "Buzz"
```

### 4. 最后补 15

```python
assert fizzbuzz(15) == "FizzBuzz"
```

---

## 代码位置

- 实现：`src/tdd_learning_python/chapter2.py`
- 测试：`tests/test_chapter2.py`
- CLI：`src/tdd_learning_python/chapter2_cli.py`
- E2E 测试：`tests/test_chapter2_cli_e2e.py`

---

## 你应该观察什么

- `1 -> 1`
- `3 -> Fizz`
- `5 -> Buzz`
- `15 -> FizzBuzz`

如果你想看更接近真实使用场景的版本，可以继续阅读 `docs/chapter-2-cli-e2e.md`，那里会展示如何把 FizzBuzz 包装成一个最小命令行程序，并用 E2E 测试模拟用户输入。

这个例子最重要的不是背规则，而是体会：

> **先让测试失败，再用最少代码通过，再在测试保护下重构。**
