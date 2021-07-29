import sys
import copy

sys.stdin = open("input.txt")

# N, M = map(int, sys.stdin.readline().strip().split())
# matrix = [sys.stdin.readline().strip() for _ in range(N)]
# 노드의 개수와 간선의 개수 입력
v, e = map(int, input().split())
print(v, e)

parent = [0] * (v+1)

# 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i]= i

def find_parent(parent, x):
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
    print(parent)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 :', end = '')
for i in range(1, v+1):
    print(find_parent(parent, i), end = ' ')
