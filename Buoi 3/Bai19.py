def so_luot_toi_thieu(a):
    n = len(a)
    dem = 0

    for i in range(n - 1):
        da_hoan_doi = False
        dem += 1

        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                da_hoan_doi = True

        if not da_hoan_doi:
            break

    return dem

a = [1, 2, 3, 5, 4]

print("Mảng ban đầu:", a)
print("Số lượt tối thiểu cần thiết:", so_luot_toi_thieu(a))