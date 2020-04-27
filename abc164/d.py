S = input()
cnt = 0
for j in range(3, len(S)+1):
    for i in range(j-3):
        if int(S[i:j]) % 2019 == 0:
            cnt += 1
print(cnt)
