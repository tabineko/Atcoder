N = int(input())
S = []
for _ in range(N):
    S.append(input())

S.sort()
dupli = 0
for i in range(N-1):
    if S[i] == S[i+1]:
        dupli += 1

print(N - dupli)
