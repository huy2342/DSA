def dem_so_lan_so_sanh(a):
    n = len(a)
    dem = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            dem += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return dem

a = [1, 2, 3]

print("Mảng ban đầu:", a)
print("Tổng số lần so sánh:", dem_so_lan_so_sanh(a))