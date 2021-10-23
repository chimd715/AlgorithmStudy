"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12954
"""
from common import print_solved


def solution(x, n):
    return [i * x for i in range(1, n+1)]


if __name__ == "__main__":
    solutions = [
        solution(2, 5),
        solution(4, 3),
        solution(-4, 2)
    ]

    answers = [
        [2, 4, 6, 8, 10],
        [4, 8, 12],
        [-4, -8]
    ]

    print_solved(solutions, answers)
