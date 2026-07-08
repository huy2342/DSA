def dem_so_lan_hoan_doi(a):
    n = len(a)
    dem = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                dem += 1

    return dem

a = [3, 2, 1]

print("Mảng ban đầu:", a)
print("Tổng số lần hoán đổi:", dem_so_lan_hoan_doi(a))