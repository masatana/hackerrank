#!/usr/bin/env python
# -*- coding: utf-8 -*-

def LEFT(l, ai):
    global al
    if len(l) == 0:
        return 0
    if l[-1] == ai:
        return al[ai]
    for j in range(len(l)):
        tmp = 0
        if al.get(ai, None) is not None:
            tmp = al[ai]
        if l[len(l)-j-tmp] > ai:
            al[ai] = len(l) - j + 1
            return len(l) - j + 1 # 1-origin
    return 0

def RIGHT(l, ai, length):
    global ar
    if len(l) == 0:
        return 0
    if l[0] == ai:
        return ar[ai]
    for k in range(len(l)):
        tmp = 0
        if ar.get(ai, None) is not None:
            tmp = ar[ai]
        if l[k+tmp] > ai:
            ar[ai] = tmp + length + k + 2
            return tmp + length + k + 2
    return 0

def INDEXPRODUCT(l):
    L = [-1 for _ in l] # L[i] represents LEFT(i)
    R = [-1 for _ in l] # R[i] represents RIGHT(i)
    for i in xrange(len(l)):
        while i != -1:
            if l[i-1] > l[i]:
                L[i] = i - 1
                break
            i = l[i] + 1
    for i in xrange(len(l)-2, -1, -1):
        idx = i+1
        while idx != -1:
            if l[idx] > l[i]:
                R[i] = idx
                break
            idx = R[idx]
    max_product = 0
    for i in xrange(len(l)):
        tmp = (L[i]+1) * (R[i] +1)
        if max_product < tmp:
            max_product = tmp
    return max_product


if __name__ == "__main__":
    N = input()
    l = [int(i) for i in input().strip().split()]
    print(INDEXPRODUCT(l))
