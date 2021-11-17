"""
    programmers algorithm
    last solved: 2021.11.17
    url: https://programmers.co.kr/learn/courses/30/lessons/12931
"""
from common import print_solved


def solution(n):
    return sum([int(num) for num in str(n)])


if __name__ == "__main__":
    solutions = [
        solution(123),
        solution(987)
    ]

    answers = [
        6,
        24
    ]

    print_solved(solutions, answers)
