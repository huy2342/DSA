def check(a, k, x):
    xe = 1
    tong = 0

    for i in a:
        if tong + i <= x:
            tong += i
        else:
            xe += 1
            tong = i
    return xe <= k
a = [1,2,3,4,5,6,7,8,9,10]
k = 5
l = max(a)
r = sum(a)
while l < r:
    mid = (l + r) // 2
    if check(a, k, mid):
        r = mid
    else:
        l = mid + 1
print(l)