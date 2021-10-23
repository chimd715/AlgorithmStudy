"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12937
"""
from common import print_solved


def solution(num):
    return "Even" if num % 2 == 0 else "Odd"


if __name__ == "__main__":
    solutions = [
        solution(3),
        solution(4)
    ]

    answers = [
        "Odd",
        "Even"
    ]

    print_solved(solutions, answers)
