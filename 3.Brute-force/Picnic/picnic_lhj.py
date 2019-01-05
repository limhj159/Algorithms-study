#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
start_time = time.time()


def picnic(_n, _m, _pairs, _friends):
    # 친구 관계가 없는 경우
    if _m == 0:
        return 0

    # 현재 set 이 학생의 수와 같은 경우
    if len(_friends) == _n:
        return 1

    _cnt = 0
    for index in range(0, len(_pairs), 2):
        _pair = set(_pairs[index:index+2])
        _interaction = _friends & _pair
        # 중복되는 친구가 없다면, 관계를 더 찾음
        if len(_interaction) == 0:
            _cnt += picnic(_n, _m, _pairs[index+2:], _friends | _pair)
        else:
            # 중복되는 경우가 있으면, 무시하고 다음 조합으로 넘어감
            continue

    return _cnt


if __name__ == "__main__":
    # n = 2
    # m = 1
    # pairs = [0, 1]

    # n = 4
    # m = 6
    # pairs = [0, 1, 1, 2, 2, 3, 0, 0, 2, 1, 3]

    n = 6
    m = 10
    pairs = [0, 1, 0, 2, 1, 2, 1, 3, 1, 4, 2, 3, 2, 4, 3, 4, 3, 5, 4, 5]

    print picnic(n, m, pairs, set())

    print time.time() - start_time

