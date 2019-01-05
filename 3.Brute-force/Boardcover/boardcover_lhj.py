#!/usr/bin/python
# -*- coding:UTF-8 -*-


import time
start_time = time.time()


d1 = [(1, 0), (0, 1), (1, 0), (1, 0)]
d2 = [(0, 1), (1, 1), (1, 1), (1, -1)]


def board_cover(_h, _w, _board):
    flag = True
    i = 0
    j = 0
    # 왼->오, 위->아래 방향으로 검은 칸의 유무를 확인하고,
    # 검은 칸이 나온 경우, 멈추고 흰 칸으로 바꾸는 시도를 한다.
    for i in xrange(_h):
        for j in xrange(_w):
            v = _board[i][j]
            if v == 0:
                flag = False
                break
        if flag is False:
            break

    if flag:
        return 1

    cnt = 0
    for k in xrange(4):
        y1 = i + d1[k][0]
        x1 = j + d1[k][1]
        y2 = i + d2[k][0]
        x2 = j + d2[k][1]

        # 게임판의 범위를 넘어가는 경우
        if x1 < 0 or x1 > _w-1 or x2 < 0 or x2 > _w-1:
            continue
        if y1 < 0 or y1 > _h-1 or y2 < 0 or y2 > _h-1:
            continue

        # 검은 칸인 경우에 흰 칸으로 바꾼다.
        if _board[y1][x1] == 0 and _board[i][j] == 0 and _board[y2][x2] == 0:

            _board[i][j] = 1
            _board[y1][x1] = 1
            _board[y2][x2] = 1

            cnt += board_cover(_h, _w, _board)

            # 다음 경우를 위해 원래대로 유지
            _board[i][j] = 0
            _board[y1][x1] = 0
            _board[y2][x2] = 0

    return cnt


if __name__ == "__main__":
    # h = 3
    # w = 7
    # board = [[-1, 0, 0, 0, 0, 0, -1],
    #          [-1, 0, 0, 0, 0, 0, -1],
    #          [-1, -1, 0, 0, 0, -1, -1]]

    # h = 3
    # w = 7
    # board = [[-1, 0, 0, 0, 0, 0, -1],
    #          [-1, 0, 0, 0, 0, 0, -1],
    #          [-1, -1, 0, 0, -1, -1, -1]]

    h = 8
    w = 10
    board = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
             [-1, 0, 0, 0, 0, 0, 0, 0, 0, -1],
             [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

    print board_cover(h, w, board)

    print time.time() - start_time