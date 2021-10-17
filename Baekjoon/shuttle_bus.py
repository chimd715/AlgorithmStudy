# 2021.10.15
# 횟수, 간격, 최대 탑승 인원
def solution(n, t, m, timetable):
    def _stringify_time(num):
        return f"{num // 60:02d}:{num % 60:02d}"

    bus_time = 540      # 09:00
    crews = []
    for time in timetable:
        crews.append(60 * int(time[:2]) + int(time[3:]))

    crews.sort()

    bus_crews = []
    for i in range(n):
        bus_info = {
            'bus_time': bus_time,
            'crews': []
        }

        crew_count = 0
        for crew in crews:
            if crew > bus_time or len(bus_info['crews']) >= m:
                break
            bus_info['crews'].append(crew)
            crew_count += 1

        for j in range(crew_count):
            crews.pop(0)
        bus_crews.append(bus_info)

        bus_time = bus_time + t

    if len(bus_crews[-1]['crews']) < m:
        return _stringify_time(bus_crews[-1]['bus_time'])
    return _stringify_time(bus_crews[-1]['crews'][-1] - 1)


# 2021.10.17
# def timestamp(str_time):
#     h = int(str_time[:2])
#     m = int(str_time[3:])
#     return h * 60 + m
#
#
# def timestamp_to_str(time):
#     return f"{time // 60:02d}:{time % 60:02d}"
#
#
# def solution(n, t, max_passenger, crew_timetable):
#     BUS_START_TIMESTAMP = timestamp("09:00")
#     BUS_END_TIMESTAMP = timestamp("23:59")
#
#     crew_timestamp_table = sorted(crew_timetable, key=lambda x: timestamp(x))
#
#     bus_timestamp = BUS_START_TIMESTAMP
#     bus_passengers = {}
#     crew_check_index = 0
#     for i in range(n):
#         if bus_timestamp > BUS_END_TIMESTAMP:
#             break
#
#         bus_time = timestamp_to_str(bus_timestamp)
#         bus_passengers[bus_time] = []
#         for bus_board_time in crew_timestamp_table[crew_check_index:]:
#             bus_board_timestamp = timestamp(bus_board_time)
#             if bus_board_timestamp > bus_timestamp or len(bus_passengers[bus_time]) >= max_passenger:
#                 break
#
#             bus_passengers[bus_time].append(bus_board_time)
#             crew_check_index += 1
#
#         bus_timestamp = bus_timestamp + t
#
#     last_bus_time = list(bus_passengers.keys())[-1]
#     last_bus_passengers = bus_passengers[last_bus_time]
#     return last_bus_time if len(last_bus_passengers) < max_passenger else timestamp_to_str(timestamp(last_bus_passengers[-1]) - 1)


solutions = [
    solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]),
    solution(2, 10, 2, ["09:10", "09:09", "08:00"]),
    solution(2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]),
    solution(1, 1, 5, 	["00:01", "00:01", "00:01", "00:01", "00:01"]),
    solution(1, 1, 1, ["23:59"]) ,
    solution(10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"])
]

solved = True
answers = ["09:00", "09:09", "08:59", "00:00", "09:00", "18:00"]
for i, sol in enumerate(solutions):
    print(sol)
    if answers[i] != sol:
        solved = False

print(solved)

"""
09 00
09 09
08 59
00 00
09 00
18 00
"""