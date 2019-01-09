#!/usr/bin/python
# -*- coding:UTF-8 -*-

import time
start_time = time.time()

q_index = 0


class Quad(object):
    def __init__(self):
        self.element = ""
        self.leaves = []

    def print_node(self):
        if self.element == 'x':
            print("x")
            for i in range(4):
                self.leaves[i].print_node()
        else:
            print(self.element)


def make_quad_tree(input_str):
    global q_index
    if input_str[q_index] == 'x':
        q_index = q_index + 1
        q = Quad()
        for i in range(4):
            q.leaves.append(make_quad_tree(input_str))
        q.element = 'x'
        return q
    else:
        q = Quad()
        q.element = input_str[q_index]
        q_index = q_index + 1
        return q


def reverse_quad_tree(quad):
    if quad.element == 'x':
        for i in range(4):
            reverse_quad_tree(quad.leaves[i])

        q1 = quad.leaves[0]
        q2 = quad.leaves[1]
        quad.leaves[0] = quad.leaves[2]
        quad.leaves[1] = quad.leaves[3]
        quad.leaves[2] = q1
        quad.leaves[3] = q2


if __name__ == "__main__":
    # input_test = "xxwwwbxwxwbbbwwxxxwwbbbwwwwbb"
    input_test = "w"
    # input_test = "xbwwb"
    # input_test = "xbwxwbbwb"
    # input_test = "xxwwwbxwxwbbbwwxxxwwbbbwwwwbb"
    root = make_quad_tree(input_test)
    reverse_quad_tree(root)
    root.print_node()


