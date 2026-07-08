def insertion_sort(arr):
    n = len(arr)

    if n <= 1:
        return  # Nếu mảng có 0 hoặc 1 phần tử, thì mảng đã được sắp xếp

    for i in range(1, n):
        key = arr[i]  # Lưu trữ phần tử hiện tại làm khóa để chèn vào đúng vị trí
        j = i - 1

        while (j >= 0 and key < arr[j]):
            # Di chuyển các phần tử lớn hơn khóa một vị trí về phía trước
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

arr = [12, 11, 13, 58, 6, 90, 55]
insertion_sort(arr)
print(arr)