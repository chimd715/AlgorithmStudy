def solution(a):
    if len(a) <= 2:
        return len(a)

    balloon_obj = []
    for i, item in enumerate(a):
        balloon_obj.append({"num": item, "index": i})
    balloon_obj.sort(key=lambda x: x["num"])

    a = min(balloon_obj[0]["index"], balloon_obj[1]["index"])
    b = max(balloon_obj[0]["index"], balloon_obj[1]["index"])
    count = 0
    for i in range(2, len(balloon_obj)):
        c = balloon_obj[i]["index"]

        if b < c or c < a:
            a = min(a, c)
            b = max(b, c)
            count += 1

    return count + 2


print(solution([3, -2, 7, 0, 4, 2, 6]))
print(solution([9, -1, -5]))
print(solution([-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]))
# 3 6
