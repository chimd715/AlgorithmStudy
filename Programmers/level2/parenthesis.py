"""
    programmers algorithm
    last solved: 2021.12.08
    url: https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3
"""
from common import print_solved


def solution(p):
    def _parse_u_v(parenthesis):
        counts = [0, 0]
        for i in range(len(parenthesis)):
            char = parenthesis[i]
            if char == "(":
                counts[0] += 1
            else:
                counts[1] += 1

            if counts[0] and counts[1] and counts[0] == counts[1]:
                return parenthesis[:i+1], parenthesis[i+1:]
        return "", parenthesis

    def _is_balanced(parenthesis):
        stack = []
        for char in parenthesis:
            if char == "(":
                stack.append(char)
            elif len(stack):
                stack.pop()
            else:
                return False

        return False if len(stack) else True

    def _reverse_parenthesis(parenthesis):
        reverse = {"(": ")", ")": "("}
        return "".join([reverse[char] for char in parenthesis])

    def _recursive_sol(parenthesis):
        if not parenthesis:
            return parenthesis

        u, v = _parse_u_v(parenthesis)
        if _is_balanced(u):
            return u + _recursive_sol(v)
        return f"({_recursive_sol(v)}){_reverse_parenthesis(u[1:-1])}"

    return _recursive_sol(p)


def short_solution(p):
    def _is_balanced(parenthesis):
        return parenthesis.count("(") == parenthesis.count(")")

    def _parse_u_v(parenthesis):
        for i in range(len(parenthesis)):
            if _is_balanced(parenthesis[:i+1]):
                return parenthesis[:i+1], parenthesis[i+1:]
        return "", parenthesis

    def _is_correct(parenthesis):
        stack = []
        for char in parenthesis:
            if char == "(":
                stack.append(char)
            elif len(stack):
                stack.pop()
            else:
                return False

        return False if len(stack) else True

    def _reverse_parenthesis(parenthesis):
        return "".join(map(lambda x: ")" if x == "(" else "(", list(parenthesis)))

    def _recursive_sol(parenthesis):
        if not parenthesis:
            return parenthesis

        u, v = _parse_u_v(parenthesis)
        if _is_correct(u):
            return u + _recursive_sol(v)
        return f"({_recursive_sol(v)}){_reverse_parenthesis(u[1:-1])}"

    return _recursive_sol(p)


if __name__ == "__main__":
    inputs = [
        "(()())()",
        ")(",
        "()))((()"
    ]

    solutions = [
        solution("(()())()"),
        solution(")("),
        solution("()))((()")
    ]

    answers = [
        "(()())()",
        "()",
        "()(())()"
    ]

    print_solved(solutions, answers)

