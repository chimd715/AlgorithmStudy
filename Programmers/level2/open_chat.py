"""
    programmers algorithm
    last solved: 2021.11.11
    url: https://programmers.co.kr/learn/courses/30/lessons/42888
"""
from common import print_solved


def solution(records):
    users = {}
    for record in records:
        record = record + " " if record.startswith("Leave") else record
        command, user_id, name = record.split(" ")

        if command == "Enter":
            users[user_id] = name
        elif command == "Change":
            users[user_id] = name

    answer = []
    for record in records:
        record = record + " " if record.startswith("Leave") else record
        command, user_id, name = record.split(" ")

        if command == "Enter":
            answer.append(f"{users[user_id]}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{users[user_id]}님이 나갔습니다.")
    return answer


if __name__ == "__main__":
    solutions = [
        solution(
            [
                "Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan",
            ]
        )
    ]

    answers = [
        ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    ]

    print_solved(solutions, answers)
