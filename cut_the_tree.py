#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict, Counter

def diff(tree, edges, points):
    sum_points = sum(points)
    ans = sum_points
    for edge in edges:
        point = 0
        visited = []
        l, r = edge
        stack = [l]
        while stack:
            ver = stack.pop(0)
            if ver not in visited and ver != r:
                visited.append(ver)
                point += points[ver-1]
                stack.extend(tree[ver])
        if ans > abs(sum_points - point-point):
            ans = abs(sum_points - point-point)
    return ans

if __name__ == "__main__":
    N = int(input())
    points = [int(i) for i in input().strip().split()]
    tree = defaultdict(list)
    edges = []
    d = Counter()
    for _ in range(N - 1):
        l, r = [int(i) for i in input().strip().split()]
        edges.append((l, r,))
        d[l] += points[r-1]
        d[r] += d[l] + points[l-1]
        tree[l].append(r)
        tree[r].append(l)
    print(d)
    print(diff(tree, edges, points))

