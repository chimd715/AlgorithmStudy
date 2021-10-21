"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/82612
"""
from common import print_solved


def solution(price, money, count):
    total_price = price * count * (count + 1) // 2
    return 0 if money >= total_price else total_price - money


if __name__ == "__main__":
    solutions = [
        solution(3, 20, 4)
    ]

    answers = [
        10
    ]

    print_solved(solutions, answers)
