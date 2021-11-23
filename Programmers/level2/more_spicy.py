"""
    programmers algorithm
    last solved: 2021.11.23
    url: https://programmers.co.kr/learn/courses/30/lessons/42626
"""
from common import print_solved


def solution(scoville, K):
    import heapq
    heap = sorted(scoville)

    count = 0
    while heap[0] < K:
        if len(heap) == 1:
            return -1
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        count += 1

    return count


def heap_solution(scoville, K):
    # fails efficiency test
    class Heap(list):
        def __init__(self):
            super().__init__()
            self.append(None)

        def top(self):
            return self[1]

        def add_new_data(self, data):
            self.append(data)

            i = len(self) - 1
            while i // 2 > 0 and self[i] < self[i//2]:
                self[i//2], self[i] = self[i], self[i//2]
                i = i // 2

        def remove_root(self):
            popped_item = self[1]
            self[1] = self[-1]
            self.pop()

            i = 1
            while i*2+1 < len(self):
                compare_index = i * 2 if self[i*2] <= self[i*2+1] else i * 2 + 1
                if self[i] > self[compare_index]:
                    self[i], self[compare_index] = self[compare_index], self[i]
                    i = compare_index
                else:
                    break
            if len(self) == i*2+1 and self[i] > self[i*2]:
                self[i], self[i*2] = self[i*2], self[i]
            return popped_item

    heap = Heap()
    heap.extend(sorted(scoville))

    count = 0
    while heap.top() < K:
        if len(heap) == 2:
            return -1
        heap.add_new_data(heap.remove_root() + (heap.remove_root() * 2))
        count += 1

    return count


def simple_solution(scoville, K):
    # fails efficiency test
    count = 0
    scoville.sort()
    while scoville[0] < K and len(scoville) > 1:
        new_food = scoville[0] + scoville[1] * 2
        scoville = [new_food] + scoville[2:]
        scoville.sort()
        count += 1

    if len(scoville) == 1 and scoville[0] < K:
        return -1
    return count


if __name__ == "__main__":
    solutions = [
        solution([1, 2, 3, 9, 10, 12], 7),
        solution([1, 2, 3, 9, 10, 12], 106)
    ]

    answers = [
        2,
        -1
    ]

    print_solved(solutions, answers)
