def sap_xep_theo_key(a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

a = [(2, "A"), (1, "B"), (2, "C")]

print("Dữ liệu ban đầu:", a)
print("Dữ liệu sau khi sắp xếp ổn định:", sap_xep_theo_key(a))