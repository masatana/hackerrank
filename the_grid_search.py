#!/usr/bin/env python
# -*- coding: utf-8 -*-

def judge(original_matrix, target_matrix, target_R, target_C):
    candidate_stack = []
    for i, row in enumerate(original_matrix):
        if len(original_matrix) - i < target_R:
            break
        if target_matrix[0][0] in row:
            for j, c in enumerate(row):
                if c == target_matrix[0][0] and len(row) - j >= target_C:
                    candidate_stack.append((i, j),)
    while candidate_stack:
        candidate = candidate_stack.pop(0)
        flg = True
        for i in range(target_R):
            for j in range(target_C):
                if original_matrix[candidate[0]+i][candidate[1]+j] != target_matrix[i][j]:
                    flg = False
                    break
            if not flg:
                break
        if flg:
            return True
    return False


if __name__ == "__main__":
    T = int(input())
    answer = []
    for _ in range(T):
        original_matrix = []
        target_matrix = []
        original_R, original_C = [int(i) for i in input().strip().split()]
        for __ in range(original_R):
            original_matrix.append([i for i in list(input().strip())])
        target_R, target_C = [int(i) for i in input().strip().split()]
        for __ in range(target_R):
            target_matrix.append([i for i in list(input().strip())])
        answer.append(judge(original_matrix, target_matrix, target_R, target_C))
    for ans in answer:
        if ans:
            print("YES")
        else:
            print("NO")

