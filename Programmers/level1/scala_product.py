"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/70128
"""
from common import print_solved


def solution(a, b):
    answer = 0
    for i, _a in enumerate(a):
        _b = b[i]

        answer += _a * _b
    return answer


def solution_2(a, b):
    return sum([x * y for x, y in zip(a, b)])


def solution_3(a, b):
    return sum([a[i] * b[i] for i in range(len(a))])


if __name__ == "__main__":
    solutions = [
        solution([1, 2, 3, 4], [-3, -1, 0, 2]),
        solution([-1, 0, 1], [1, 0, -1]),
    ]

    answers = [3, -2]

    print_solved(solutions, answers)
