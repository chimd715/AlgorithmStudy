"""
    programmers algorithm
    last solved: 2021.10.22
    url: https://programmers.co.kr/learn/courses/30/lessons/12928
"""
from common import print_solved


def find_divisors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def solution(n):
    return sum(find_divisors(n))


if __name__ == "__main__":
    solutions = [solution(12), solution(5)]

    answers = [28, 6]

    print_solved(solutions, answers)
