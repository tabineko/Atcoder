# N = int(input())
# S = input()
# count = 0
#
# for i in range(0, N-2):
#     for j in range(i+1, N-1):
#         if S[i] == S[j]:
#             continue
#         for k in range(j+1, N):
#             if S[i] == S[k] or S[j] == S[k]:
#                 continue
#             if j-i != k-j:
#                 count += 1
#
# print(count)
N, K = map(int, input().split())
mod = (10**9+7)
cnt = [0]*(K+1)

def gcd(a,b):
    if a % b == 0:
        return b
    return gcd(b, a%b)

for i in range(K, 0, -1):
    cnt[i] += pow(K//i, N, mod)
    for j in range(2, K//i+1):
        cnt[i] -= cnt[i*j]

ans = 0

for i in range(1, K+1):
    ans += i*(cnt[i])%mod
    ans %= mod

print(ans)
