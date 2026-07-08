def sap_xep_on_dinh(a):
    n = len(a)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if a[j][0] > a[j + 1][0]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

a = [(2, "a"), (1, "b"), (2, "c")]

print("Danh sách ban đầu:", a)
print("Danh sách sau khi sắp xếp:", sap_xep_on_dinh(a))
print("Các phần tử có khóa bằng nhau vẫn giữ nguyên thứ tự.")