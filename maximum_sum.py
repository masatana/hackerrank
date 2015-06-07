#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solve(M, arr):
    _max = 0
    prefix = [0 for _ in arr]
    prefix.insert(0, 0)
    cur = 0
    for i, v in enumerate(arr):
        cur = (v + cur) % M
        prefix[i] = cur
    for i in range(len(arr)):
        for j in range(i-1,0,-1):
            _max = max(_max, (prefix[i]-prefix[j]+M)%M)
        _max = max(_max, prefix[i])
    return _max

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, M = [int(i) for i in input().strip().split()]
        arr = [int(i) for i in input().strip().split()]
        print(solve(M, arr))

