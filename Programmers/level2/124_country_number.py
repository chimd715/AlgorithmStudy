"""
    programmers algorithm
    last solved: 2021.11.17
    url: https://programmers.co.kr/learn/courses/30/lessons/12899
"""
from common import print_solved


def solution(n):
    rebase = ["4", "1", "2"]
    based_num = ""
    while n > 0:
        n, remainder = divmod(n, 3)
        if remainder == 0:
            n -= 1
        based_num = str(rebase[remainder]) + based_num
    return based_num


def solution_2(n):
    rebase = ["1", "2", "4"]
    based_num = ""
    while n > 0:
        n, remainder = divmod(n-1, 3)
        based_num = str(rebase[remainder]) + based_num
    return based_num


if __name__ == "__main__":
    solutions = [
        solution(1),
        solution(2),
        solution(3),
        solution(4),
        solution(5),
        solution(6),
        solution(7),
        solution(8),
        solution(9),
        solution(10),
        solution(11)
    ]

    answers = [
        "1",
        "2",
        "4",
        "11",
        "12",
        "14",
        "21",
        "22",
        "24",
        "41",
        "42"
    ]

    print_solved(solutions, answers)
