def sap_xep_giam_dan(a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] < a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

a = [5, 1, 4, 2, 8]

print("Mảng ban đầu:", a)
print("Mảng sau khi sắp xếp giảm dần:", sap_xep_giam_dan(a))