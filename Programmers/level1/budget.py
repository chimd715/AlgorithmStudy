"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/12982
"""
from common import print_solved


def solution(d, budget):
    d.sort()

    supported_dept_list = []
    for demand in d:
        if budget < demand:
            break
        supported_dept_list.append(demand)
        budget -= demand

    return len(supported_dept_list)


if __name__ == "__main__":
    solutions = [
        solution([1, 3, 2, 5, 4], 9),
        solution([2, 2, 3, 3], 10),
    ]

    answers = [3, 4]

    print_solved(solutions, answers)
