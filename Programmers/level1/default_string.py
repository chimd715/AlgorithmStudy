"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12918
"""
from common import print_solved
import re


def solution(s):
    if len(s) not in [4, 6]:
        return False
    return False if re.search(r"[^0-9]", s) else True


if __name__ == "__main__":
    solutions = [solution("a234"), solution("1324")]

    answers = [False, True]

    print_solved(solutions, answers)
