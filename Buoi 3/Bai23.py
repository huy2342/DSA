def thong_ke_bubble_sort(a):
    n = len(a)

    so_sanh = 0
    hoan_doi = 0

    for i in range(n - 1):
        for j in range(n - 1 - i):

            so_sanh += 1

            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                hoan_doi += 1

    return so_sanh, hoan_doi


a = [5, 4, 3, 2, 1]

ss, hd = thong_ke_bubble_sort(a)

print("Số lần so sánh:", ss)
print("Số lần hoán đổi:", hd)