N, Y = map(int, input().split())
x = y = z = -1
b = (2*N + 7*Y) % 9
c = N - b
a = (Y - 5000*b -1000*c)/9000
c = c - a
if (Y == 10000*a + 5000*b + 1000*c and a >= 0 and c >= 0):
    x = int(a)
    y = int(b)
    z = int(c)

print(x, y, z)

# N, Y = map(int, input().split())
# x = y = z = -1
# b = (2*N + 7*Y) % 9
# c = N - b
# a = (Y - 5000*b -1000*c)/9000
# if (Y == 9000*a + 5000*b + 1000*c and a >= 0 and a <= c):
#     x = int(a)
#     y = int(b)
#     z = int(c - a)
#
# print(x, y, z)
