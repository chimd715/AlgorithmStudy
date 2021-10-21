"""
    programmers algorithm
    last solved: 2021.10.18
    url: https://programmers.co.kr/learn/courses/30/lessons/68935
"""
from common import print_solved


def change_base(n, base):
    changed_n = ""
    while n > 0:
        """
            quotient = n // base
            remainder = n % base
    
            n = quotient
            changed_n = str(remainder) + changed_n
            
            ==>
            
            n, r = divmod(n, base)
            changed_n = str(r) + changed_n
        """
        n, r = divmod(n, base)
        changed_n = str(r) + changed_n
    return changed_n


def solution(n):
    reversed_ternary_n = change_base(n, 3)[::-1]
    return int(reversed_ternary_n, 3)


if __name__ == "__main__":
    solutions = [
        solution(45),
        solution(125)
    ]

    answers = [
        7,
        229
    ]

    print_solved(solutions, answers)
