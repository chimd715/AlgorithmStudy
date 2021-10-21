"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/87389
"""
from common import print_solved


def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i
    return -1


if __name__ == "__main__":
    solutions = [
        solution(10),
        solution(12)
    ]

    answers = [
        3,
        11
    ]

    print_solved(solutions, answers)
