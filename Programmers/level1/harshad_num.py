"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12947
"""
from common import print_solved


def solution(x):
    return x % sum([int(num) for num in str(x)]) == 0


if __name__ == "__main__":
    solutions = [
        solution(10),
        solution(12),
        solution(11),
        solution(13)
    ]

    answers = [
        True,
        True,
        False,
        False
    ]

    print_solved(solutions, answers)
