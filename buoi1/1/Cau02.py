def tuyen_tinh(array, n, x):

    for i in range(n):
        if array[i] == x:
            return i

    return -1


# Ví dụ 1
array = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
x = 110
n = len(array)

result = tuyen_tinh(array, n, x)

if result != -1:
    print("Phan tu duoc tim thay tai vi tri:", result)
else:
    print("Khong tim thay phan tu")


# Ví dụ 2
array = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
x = 185
n = len(array)

result = tuyen_tinh(array, n, x)

if result != -1:
    print("Phan tu duoc tim thay tai vi tri:", result)
else:
    print("Khong tim thay phan tu")