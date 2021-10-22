"""
    programmers algorithm
    last solved: 2021.10.22
    url: https://programmers.co.kr/learn/courses/30/lessons/12932
"""
from common import print_solved


def solution(n):
    return [int(num) for num in str(n)][::-1]


if __name__ == "__main__":
    solutions = [
        solution(12345),
        solution(10000000000)
    ]

    answers = [
        [5, 4, 3, 2, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    ]

    print_solved(solutions, answers)
