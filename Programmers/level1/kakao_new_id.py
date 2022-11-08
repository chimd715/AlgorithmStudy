"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/72410
"""
from common import print_solved
import re


def remove_first_last_dot(string):
    if string.startswith("."):
        string = string[1:]
    if string.endswith("."):
        string = string[:-1]
    return string


def solution(new_id):
    # phase1 : lower case
    answer = new_id.lower()

    # phase2 : remove all char except [a-z]\d[-_.]
    answer = re.sub(r"[^a-z0-9-_.]*", "", answer)

    # phase3 : replace continued '.' to one '.'
    answer = re.sub(r"[.]{2,}", ".", answer)

    # phase4 : remove first and last '.'
    answer = remove_first_last_dot(answer)

    # phase5 : if empty, put a
    if not answer:
        answer = "aaa"

    # phase6 : if length of id is longer than 16 then remove last characters until id's length is 15 and redo phase 4
    if len(answer) > 15:
        answer = remove_first_last_dot(answer[:15])

    # phase7 : if length of id is less then or equal to 2, then repeat last character of id until new_id's length is 3
    while len(answer) <= 2:
        answer += answer[-1]

    return answer


if __name__ == "__main__":
    solutions = [
        solution("...!@BaT#*..y.abcdefghijklm"),
        solution("z-+.^."),
        solution("=.="),
        solution("123_.def"),
        solution("abcdefghijklmn.p"),
    ]

    answers = ["bat.y.abcdefghi", "z--", "aaa", "123_.def", "abcdefghijklmn"]

    print_solved(solutions, answers)
