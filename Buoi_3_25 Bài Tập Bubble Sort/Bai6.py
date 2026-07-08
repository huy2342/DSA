def phan_tu_cuoi_sau_mot_luot(a):
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

    return a[-1]


a = [4, 2, 7, 1, 3]

print("Mảng ban đầu:", a)
print("Phần tử cuối sau 1 lượt:", phan_tu_cuoi_sau_mot_luot(a))