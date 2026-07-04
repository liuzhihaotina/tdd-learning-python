import pytest

from tdd_learning_python.chapter2 import fizzbuzz


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, 1),
        (2, 2),
        (3, "Fizz"),
        (4, 4),
        (5, "Buzz"),
        (15, "FizzBuzz"),
        (30, "FizzBuzz"),
    ],
)
def test_fizzbuzz(number: int, expected: int | str) -> None:
    assert fizzbuzz(number) == expected
