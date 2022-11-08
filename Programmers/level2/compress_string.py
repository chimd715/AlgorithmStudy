"""
    programmers algorithm
    last solved: 2021.10.24
    url: https://programmers.co.kr/learn/courses/30/lessons/60057
"""
from common import print_solved


def compress(s, size):
    tokens = [s[size * i : size * i + size] for i in range(len(s) // size + 2)]
    count = 0
    current_comparison = tokens[0]
    compressed_string = ""
    for i, token in enumerate(tokens):
        if current_comparison == token and i != len(tokens) - 1:
            count += 1
            continue
        compressed_string += (
            f"{count}{current_comparison}" if count > 1 else current_comparison
        )
        current_comparison = token
        count = 1
    return compressed_string


def solution(s):
    return min([len(compress(s, i)) for i in range(1, len(s) + 1)])


if __name__ == "__main__":
    solutions = [
        solution("aabbaccc"),
        solution("ababcdcdababcdcd"),
        solution("abcabcdede"),
        solution("abcabcabcabcdededededede"),
        solution("xababcdcdababcdcd"),
    ]

    answers = [7, 9, 8, 14, 17]

    print_solved(solutions, answers)
