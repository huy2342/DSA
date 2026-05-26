def linearsearch(arr, key):

    for i in range(len(arr)):
        if arr[i] == key:
            return i

    return -1


arr = ['Bao', 'An', 'Dat', 'Duc', 'Hung', 'Phi', 'Vinh', 'Dung']

key = 'Phi'

kq = linearsearch(arr, key)

if kq != -1:
    print("Phan tu tim thay tai vi tri:", kq)
else:
    print("Khong tim thay phan tu")