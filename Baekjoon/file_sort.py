import re


def solution(files):
    disassembled_files = []
    for file in files:
        res = re.search(r'\d{1,}', file)

        head = file[:res.start()]
        number = res.group()
        tail = file[res.end()+1:]

        disassembled_files.append({
            "origin_name": file,
            "head": head,
            "number": number,
            "tail": tail
        })

    answer = []
    for file_obj in sorted(disassembled_files, key=lambda x: (x["head"].lower(), int(x["number"]))):
        answer.append(file_obj["origin_name"])

    return answer


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]

if solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]) == ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"] \
        and solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]) == ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]:
    print("solved")
