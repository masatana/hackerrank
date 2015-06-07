#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

if __name__ == "__main__":
    input()
    A = Counter()
    for i in input().strip().split():
        A[int(i)] += 1
    input()
    B = Counter()
    for i in input().strip().split():
        B[int(i)] += 1
    answer = set()
    for i in A:
        if A[i] != B[i]:
            answer.add(str(i))
    print(" ".join(sorted(answer)))

