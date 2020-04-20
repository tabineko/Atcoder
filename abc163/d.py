N, K = map(int, input().split())

total = 0
mod = 10**9+7
s = [0]
for i in range(0, N+1):
    s.append(s[-1] + i)

for i in range(K, N+2):
    total = (total + ((s[-1]-s[-(i+1)]) - s[i] + 1)) % mod
print(total)
