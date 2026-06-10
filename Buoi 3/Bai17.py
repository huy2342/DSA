def sap_xep_k_phan_tu_lon_nhat(a, k):
    n = len(a)

    for i in range(k):
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

a = [3, 1, 4, 1, 5]
k = 2

print("Mảng ban đầu:", a)
print("Mảng sau", k, "lượt Bubble Sort:", sap_xep_k_phan_tu_lon_nhat(a, k))