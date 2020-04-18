N, K = map(int, input().split())

N %= K

while abs(N - K) < N:
    N = abs(N - K)

print(N)
