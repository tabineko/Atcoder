import queue
K = int(input())

q = queue.Queue()

for i in range(1,10):
    q.put(i)

for _ in range(K-1):
    n = q.get()
    if n % 10 != 0:
        q.put(10*n + (n%10) - 1)
    q.put(10*n + n%10)
    if n % 10 != 9:
        q.put(10*n + (n%10) + 1)

print(q.get())
