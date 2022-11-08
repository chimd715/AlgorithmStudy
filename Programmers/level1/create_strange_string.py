"""
    programmers algorithm
    last solved: 2021.10.23
    url: https://programmers.co.kr/learn/courses/30/lessons/12930
"""
from common import print_solved


def solution(s):
    answer = []
    for word in s.split(" "):
        new_word = ""
        for i, char in enumerate(word):
            new_word += char.upper() if i % 2 == 0 else char.lower()
        answer.append(new_word)
    return " ".join(answer)


if __name__ == "__main__":
    solutions = [solution("try hello world")]

    answers = ["TrY HeLlO WoRlD"]

    print_solved(solutions, answers)
