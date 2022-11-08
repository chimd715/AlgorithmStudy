"""
    programmers algorithm
    last solved: 2021.10.28
    url: https://programmers.co.kr/learn/courses/30/lessons/12919
"""
from common import print_solved


def solution(seoul):
    return f"김서방은 {seoul.index('Kim')}에 있다"


if __name__ == "__main__":
    solutions = [solution(["Jane", "Kim"])]

    answers = [1]

    print_solved(solutions, answers)
