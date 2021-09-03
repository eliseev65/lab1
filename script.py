from collections import deque

# from time import time
# start_time = time()

xx = [-2, -1, 1, 2, 2, 1, -1, -2]
yy = [1, 2, 2, 1, -1, -2, -2, -1]


n, m = 80, 80 #int(input()), int(input())
x1, y1 = 0, 0
x2, y2 = 70, 70

a = [[100500 for j in range(m)] for i in range(n)]

q = deque()
q.append(x1)
q.append(y1)
a[x1][y1] = 0


while len(q):
    x = q.popleft()
    y = q.popleft()
    for i in range(8):
        f = 0 <= x + xx[i] < n and 0 <= y + yy[i] < m
        if f and a[x][y] + 1 < a[x + xx[i]][y + yy[i]]:
            a[x + xx[i]][y + yy[i]] = a[x][y] + 1
            q.append(x + xx[i])
            q.append(y + yy[i])

print(a[x2][y2])
# for i in range(n):
#     print(a[i])

# print(time() - start_time)