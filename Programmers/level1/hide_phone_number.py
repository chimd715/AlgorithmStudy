"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12948
"""
from common import print_solved


def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


if __name__ == "__main__":
    solutions = [solution("01033334444"), solution("027778888")]

    answers = ["*******4444", "*****8888"]

    print_solved(solutions, answers)
