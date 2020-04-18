N = int(input())
x = [0]
y = [0]
t = [0]
for _ in range(N):
    a, b, c = map(int, input().split())
    t.append(a)
    x.append(b)
    y.append(c)

poss = "Yes"

for i in range(N):
    d = abs(x[i+1]-x[i]) + abs(y[i+1]-y[i])
    td = t[i+1]-t[i]
    if td < d:
        poss = "No"
        break
    if d % 2 != td % 2:
        poss = "No"
        break

print(poss)
