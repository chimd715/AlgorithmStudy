"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/81301
"""
from common import print_solved


def solution(s):
    number_change_form = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    for key in number_change_form:
        s = s.replace(key, str(number_change_form[key]))

    return int(s)


if __name__ == "__main__":
    solutions = [
        solution("one4seveneight"),
        solution("23four5six7"),
        solution("2three45sixseven"),
        solution("123"),
    ]

    answers = [1478, 234567, 234567, 123]

    print_solved(solutions, answers)
