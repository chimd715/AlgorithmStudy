"""
    programmers algorithm
    last solved: 2022.11.08
    url: https://school.programmers.co.kr/learn/courses/30/lessons/92334
"""
from common import print_solved


def solution(id_list: list, reports: list, k: int) -> list:
    reported_by_id: dict = {user_id: set() for user_id in id_list}
    mail_inbox: dict = {user_id: [] for user_id in id_list}

    for report in reports:
        reporter, reportee = report.split(" ")
        reported_by_id[reportee].add(reporter)

    for reportee, reporters in reported_by_id.items():
        if len(reporters) < k:
            continue

        for reporter in reporters:
            mail_inbox[reporter].append(reportee)

    return [len(mails) for mails in mail_inbox.values()]


if __name__ == "__main__":
    solutions = [
        solution(
            ["muzi", "frodo", "apeach", "neo"],
            ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
            2,
        ),
        solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3),
    ]

    answers = [[2, 1, 1, 0], [0, 0]]

    print_solved(solutions, answers)
