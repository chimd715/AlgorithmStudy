"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12917
"""
from common import print_solved


def solution(s):
    return ''.join(sorted([char for char in s], key=lambda x: ord(x), reverse=True))


if __name__ == "__main__":
    solutions = [
        solution("Zbcdefg")
    ]

    answers = [
        "gfedcbZ"
    ]

    print_solved(solutions, answers)
