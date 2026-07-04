# 第四章实战示例：从类与对象开始写测试

这一章用“银行账户”来练习如何测试**有状态对象**。

---

## 为什么从对象开始

当逻辑开始涉及状态变化时，单纯的纯函数示例就不够了。这时可以引入对象来表示状态，并通过测试验证状态变化前后是否正确。

---

## 需求

- 可以存款
- 可以取款
- 余额不能为负数
- 取款超出余额时应报错

---

## 推荐的 TDD 顺序

### 1. 先写初始余额

```python
account = BankAccount()
assert account.balance == 0
```

### 2. 再写存款

```python
account.deposit(50)
assert account.balance == 50
```

### 3. 再写取款

```python
account.withdraw(20)
assert account.balance == 30
```

### 4. 最后补异常分支

```python
with pytest.raises(ValueError, match="余额不足"):
    account.withdraw(100)
```

---

## 代码位置

- 实现：`src/tdd_learning_python/chapter4.py`
- 测试：`tests/test_chapter4.py`

---

## 你应该观察什么

- 对象的初始状态
- 每次方法调用后状态如何变化
- 非法输入如何被拒绝

这个例子要让你体会：

> **对象本身就是状态的载体，而测试的重点是状态变化是否符合预期。**
