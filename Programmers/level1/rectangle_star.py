"""
    programmers algorithm
    last solved: 2021.10.22
    url: https://programmers.co.kr/learn/courses/30/lessons/12969
"""
from common import print_solved


def solution(a, b):
    # a, b = map(int, input().strip().split(' '))
    for line in ["*" * a] * b:
        print(line)


if __name__ == "__main__":
    solution(5, 3)
