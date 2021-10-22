"""
    programmers algorithm
    last solved: 2021.10.22
    url: https://programmers.co.kr/learn/courses/30/lessons/12926
"""
from common import print_solved
import re


def shift_str(s):
    answer = ""
    for char in s:
        if ord('a') <= ord(char) < ord('z'):
            answer += chr(ord(char) + 1)
        elif char == 'z':
            answer += 'a'
        elif ord('A') <= ord(char) < ord('Z'):
            answer += chr(ord(char) + 1)
        elif char == 'Z':
            answer += 'A'
        else:
            answer += char
    return answer


def solution(s, n):
    answer = s
    for i in range(n):
        answer = shift_str(answer)
    return answer


if __name__ == "__main__":
    solutions = [
        solution("AB", 1),
        solution("z", 1),
        solution("a B z", 4)
    ]

    answers = [
        "BC",
        "a",
        "e F d"
    ]

    print_solved(solutions, answers)
