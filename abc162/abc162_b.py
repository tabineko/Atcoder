N = int(input())
total = 0
for i in range(N):
    if ((i+1)%3 != 0) & ((i+1)%5 != 0):
        total += (i+1)

print(total)
