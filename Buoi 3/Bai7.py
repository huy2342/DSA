def sap_xep_ky_tu(a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

a = ['d', 'a', 'c', 'b']

print("Mảng ký tự ban đầu:", a)
print("Mảng ký tự sau khi sắp xếp:", sap_xep_ky_tu(a))