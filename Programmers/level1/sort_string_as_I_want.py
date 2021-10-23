"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12915
"""
from common import print_solved


def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))


if __name__ == "__main__":
    solutions = [
        solution(["sun", "bed", "car"], 1),
        solution(["abce", "abcd", "cdx"], 2)
    ]

    answers = [
        ["car", "bed", "sun"],
        ["abcd", "abce", "cdx"]
    ]

    print_solved(solutions, answers)
