"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12916
"""
from common import print_solved


def solution(s):
    p_count = 0
    y_count = 0
    for char in s.lower():
        if char == "p":
            p_count += 1
        elif char == "y":
            y_count += 1
    return p_count == y_count


def solution_2(s):
    lower_s = s.lower()
    return lower_s.count("p") == lower_s.count("y")


def solution_3(s):
    from collections import Counter

    counter = Counter(s.lower())
    return counter["p"] == counter["y"]


if __name__ == "__main__":
    solutions = [solution("pPoooyY"), solution("Pyy")]

    answers = [True, False]

    print_solved(solutions, answers)
