"""
    programmers algorithm
    last solved: 2021.11.17
    url: https://programmers.co.kr/learn/courses/30/lessons/12901
"""
from common import print_solved


def solution(a, b):
    from datetime import date
    return date(2016, a, b).ctime()[:3].upper()


def solution_2(a, b):
    # 각 달마다 며칠까지 있는지 안다고 가정
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1]) + b-1) % 7]


def solution_3(a, b):
    from datetime import datetime
    days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    return days[datetime.strptime(f"2016-{a}-{b}", "%Y-%m-%d").weekday()]


if __name__ == "__main__":
    solutions = [
        solution(5, 24)
    ]

    answers = [
        "TUE"
    ]

    print_solved(solutions, answers)
