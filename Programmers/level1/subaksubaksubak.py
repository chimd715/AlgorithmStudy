"""
    programmers algorithm
    last solved: 2021.10.21
    url: https://programmers.co.kr/learn/courses/30/lessons/12922
"""
from common import print_solved


def solution(n):
    answer = ""
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += "박"
        else:
            answer += "수"
    return answer


def solution_2(n):
    n_len = n // 2 + 1
    answer = "수박" * n_len
    return answer[:n]


if __name__ == "__main__":
    solutions = [solution(3), solution(4)]

    answers = ["수박수", "수박수박"]

    print_solved(solutions, answers)
