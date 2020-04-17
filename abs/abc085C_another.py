N, Y = map(int, input().split())
x = y = z = -1
for i in range(N+1):
    for j in range(N+1-i):
        k = N - (i+j)
        if 10000*i + 5000*j + 1000*k == Y:
            x = i
            y = j
            z = k

print(x, y, z)
