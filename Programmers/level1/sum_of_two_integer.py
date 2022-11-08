"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12912
"""
from common import print_solved


def solution(a, b):
    return sum(range(a, b + 1)) if a <= b else sum(range(b, a + 1))


def solution_2(a, b):
    a, b = (a, b) if a < b else (b, a)
    sum_a = (a - 1) * a / 2
    sum_b = b * (b + 1) / 2
    return sum_b - sum_a


if __name__ == "__main__":
    solutions = [solution(3, 5), solution(3, 3), solution(5, 3)]

    answers = [12, 3, 12]

    print_solved(solutions, answers)
