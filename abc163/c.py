N = int(input())
A = list(map(int, input().split()))
cnt = []
[cnt.append(0) for _ in range(len(A))]

for i in A:
    cnt[i-1] += 1

for i in range(N-1):
    print(cnt[i])

print("0")
