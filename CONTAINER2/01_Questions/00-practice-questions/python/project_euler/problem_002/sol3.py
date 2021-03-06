"""
Project Euler Problem 2: https://projecteuler.net/problem=2

Even Fibonacci Numbers

Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.

References:
    - https://en.wikipedia.org/wiki/Fibonacci_number
"""


def solution(n: int = 4000000) -> int:
    """
    Returns the sum of all even fibonacci sequence elements that are lower
    or equal to n.

    >>> solution(10)
    10
    >>> solution(15)
    10
    >>> solution(2)
    2
    >>> solution(1)
    0
    >>> solution(34)
    44
    """

    if n <= 1:
        return 0
    a = 0
    b = 2
    count = 0
    while 4 * b + a <= n:
        a, b = b, 4 * b + a
        count += a
    return count + b


if __name__ == "__main__":
    print(f"{solution() = }")
