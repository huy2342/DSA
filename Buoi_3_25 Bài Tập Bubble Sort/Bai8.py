def kiem_tra_sau_k_luot(a, k):
    n = len(a)

    for i in range(min(k, n - 1)):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a == sorted(a)

a = [3, 2, 1]
k = 1

print("Mảng ban đầu:", a)
print("Đã sắp xếp hoàn toàn chưa:", kiem_tra_sau_k_luot(a, k))