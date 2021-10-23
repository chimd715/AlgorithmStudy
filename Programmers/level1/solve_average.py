"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12944
"""
from common import print_solved


def solution(arr):
    return sum(arr) / len(arr)


if __name__ == "__main__":
    solutions = [
        solution([1, 2, 3, 4]),
        solution([5, 5])
    ]

    answers = [
        2.5,
        5
    ]

    print_solved(solutions, answers)
