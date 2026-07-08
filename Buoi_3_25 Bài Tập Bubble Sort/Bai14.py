def cocktail_shaker_sort(a):
    trai = 0
    phai = len(a) - 1

    while trai < phai:

        for i in range(trai, phai):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]

        phai -= 1

        for i in range(phai, trai, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]

        trai += 1

    return a

a = [5, 1, 4, 2, 8]

print("Mảng ban đầu:", a)
print("Mảng sau Cocktail Shaker Sort:", cocktail_shaker_sort(a))