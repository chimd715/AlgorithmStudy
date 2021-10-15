class Queue(list):
    def pop_left(self):
        popped_item = self.pop(0)
        return popped_item

    def shift(self):
        popped_item = self.pop(0)
        self.append(popped_item)


def solution(priorities, location):
    print_queue = Queue(priorities)
    count = 0

    while True:
        max_priority = max(print_queue)
        if max_priority == print_queue[0]:
            # print item
            count += 1
            if location == 0:
                break
            else:
                print_queue.pop_left()
                location -= 1
        else:
            # shift item
            print_queue.shift()
            if location == 0:
                location += len(print_queue) - 1
            else:
                location -= 1

    return count


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
# 1 5
