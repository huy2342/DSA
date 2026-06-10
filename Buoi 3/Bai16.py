def dem_nghich_the(a):
    dem = 0

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] > a[j]:
                dem += 1

    return dem

a = [2, 3, 1]

print("Mảng ban đầu:", a)
print("Số nghịch thế:", dem_nghich_the(a))
print("Số lần swap của Bubble Sort:", dem_nghich_the(a))