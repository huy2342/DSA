# Bài 17. Tìm kiếm có lính canh

def tim_kiem_linh_canh(a, x):
    a.append(x)

    i = 0

    while a[i] != x:
        i += 1

    a.pop()

    if i < len(a):
        return i

    return -1


a = [7, 3, 9, 12, 5]

x = int(input("Nhap x: "))

print("Ket qua:", tim_kiem_linh_canh(a, x))
