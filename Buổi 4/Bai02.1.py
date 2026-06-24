def insertion_s(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        # Di chuyển các phần tử của arr[0..i-1], lớn hơn key,
        # đến một vị trí phía trước vị trí hiện tại
        j = i - 1

        while (j >= 0 and key < arr[j]):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

arr = [12, 31, 130, 15, 18, 150, 30]

insertion_s(arr)

for i in range(len(arr)):
    print("% d" % arr[i])