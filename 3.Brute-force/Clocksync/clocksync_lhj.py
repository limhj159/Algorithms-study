#!/usr/bin/python
# -*- coding:UTF-8 -*-

from __future__ import print_function

import time
start_time = time.time()

switch_info = [[0, 1, 2],
               [3, 7, 9, 11],
               [4, 10, 14, 15],
               [0, 4, 5, 6, 7],
               [6, 7, 8, 10, 12],
               [0, 2, 14, 15],
               [3, 14, 15],
               [4, 5, 7, 14, 15],
               [1, 2, 3, 4, 5],
               [3, 4, 5, 9, 13]]


def clock_sync(_input, _candidate_index, _index_list, _size):
    if _size == 0:
        # print(_candidate_index)
        for index in _candidate_index:
            switch_clocks = switch_info[index]
            for clock_index in switch_clocks:
                update_val = _input[clock_index] + 3
                if update_val > 12:
                    update_val = 3
                _input[clock_index] = update_val
        # print(_input)

        flag = False
        for clock in _input:
            if clock != 12:
                flag = True

        if flag:
            for index in _candidate_index:
                switch_clocks = switch_info[index]
                for clock_index in switch_clocks:
                    update_val = _input[clock_index] - 3
                    if update_val < 3:
                        update_val = 12
                    _input[clock_index] = update_val
            return False
        else:
            return True
        # return 1

    else:
        # cnt = 0
        for _index in _index_list:
            _candidate_index.append(_index)
            # cnt += clock_sync(_input, _candidate_index, _index_list, _size-1)
            _result = clock_sync(_input, _candidate_index, _index_list, _size-1)
            _candidate_index.remove(_index)

            if _result:
                return True

        return False
        # return cnt


if __name__ == "__main__":
    input_list = [12, 6, 6, 6, 6, 6, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
    # input_list = [12, 9, 3, 12, 6, 6, 9, 3, 12, 9, 12, 9, 12, 12, 6, 6]

    result = clock_sync(input_list, list(), range(10), 1)
    print(result)

    #
    # for i in range(1, 11):
    #     result = clock_sync(input_list, list(), range(10), i)
    #     if result is True:
    #         print(i)
    #         break

