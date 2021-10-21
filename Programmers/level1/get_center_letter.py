"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12903
"""
from common import print_solved


def solution(s):
    if len(s) % 2 == 0:
        start = len(s) // 2 - 1
        end = len(s) // 2 + 1
        return s[start:end]
    return s[len(s)//2]


def short_solution(s):
    return s[(len(s) - 1)//2:len(s) // 2 + 1]


if __name__ == "__main__":
    solutions = [
        solution("abcde"),
        solution("qwer")
    ]

    answers = [
        "c",
        "we"
    ]

    print_solved(solutions, answers)
