from collections import deque

a = [4,2,12,11,-5,8,1,5,6]
k = 3

q = deque()
res = []

for i in range(len(a)):
    while q and q[0] <= i-k:
        q.popleft()

    while q and a[q[-1]] >= a[i]:
        q.pop()

    q.append(i)

    if i >= k-1:
        res.append(a[q[0]])

print(res)