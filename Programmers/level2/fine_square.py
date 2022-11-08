"""
    programmers algorithm
    last solved: 2021.11.17
    url: https://programmers.co.kr/learn/courses/30/lessons/62048
"""
from common import print_solved


def solution(w, h):
    def _find_gcd(a, b):
        _gcd = 1
        for _i in range(2, min(a, b) + 1):
            if a % _i == 0 and b % _i == 0:
                _gcd = max(_gcd, _i)
        return _gcd

    return w * h - (w + h - _find_gcd(w, h))


if __name__ == "__main__":
    solutions = [solution(8, 12)]

    answers = [80]

    print_solved(solutions, answers)
