N, M = map(int, input().split())
A = list(map(int, input().split()))
d = -1

if sum(A) <= N:
    d = N - sum(A)

print(d)
