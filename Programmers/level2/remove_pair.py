"""
    programmers algorithm
    last solved: 2021.11.27
    url: https://programmers.co.kr/learn/courses/30/lessons/12973
"""
from common import print_solved


def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
            continue
        stack.append(char)

    return 0 if stack else 1


def recursion_solution(s):
    # recursion depth limit (s length upto 1000000)
    def _remove_repeated_char(s):
        if len(s) < 2:
            return s

        previous = s[0]
        for i, char in enumerate(s[1:]):
            if previous == char:
                return _remove_repeated_char(s[:i] + s[i+2:])
            previous = char

        return s

    return 0 if len(_remove_repeated_char(s)) else 1


if __name__ == "__main__":
    solutions = [
        solution("baabaa"),
        solution("baaba"),
        solution("a"),
        solution("a" * 1000000),
        solution("cdcd")
    ]

    answers = [
        1,
        0,
        0,
        1,
        0
    ]

    print_solved(solutions, answers)
