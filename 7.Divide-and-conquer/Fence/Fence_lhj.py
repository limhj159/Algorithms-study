#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
start_time = time.time()

boxes = [0] * 2000


def max_rec(start, end):
    if start == end:
        return boxes[end]

    middle = (start + end) / 2
    tmp = max(max_rec(start, middle), max_rec(middle+1, end))

    width = 1
    height = boxes[middle]
    left = middle - 1
    right = middle + 1
    tmp = max(tmp, width * height)
    while left >= start or right <= end:
        if left < start or \
                (boxes[left] <= boxes[right] and right <= end):
            height = min(height, boxes[right])
            right = right + 1
            width = width + 1
            tmp = max(tmp, width * height)
        elif right > end or \
                (boxes[left] > boxes[right] and left >= start):
            height = min(height, boxes[left])
            left = left - 1
            width = width + 1
            tmp = max(tmp, width * height)
        else:
            break

    return tmp


if __name__ == "__main__":
    # n = 7
    # input_list = [7, 1, 5, 9, 6, 7, 3]
    n = 7
    input_list = [1, 4, 4, 4, 4, 1, 1]
    # n = 4
    # input_list = [1, 8, 2, 2]
    for i, e in enumerate(input_list):
        boxes[i] = e

    print(max_rec(0, n-1))
