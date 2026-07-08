def dem_so_luot_can_thiet(a):
    n = len(a)
    so_luot = 0

    for i in range(n - 1):
        da_hoan_doi = False
        so_luot += 1

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_hoan_doi = True

        if not da_hoan_doi:
            break

    return so_luot

a = [2, 1, 3, 4]

print("Mảng ban đầu:", a)
print("Số lượt cần để sắp xếp:", dem_so_luot_can_thiet(a))