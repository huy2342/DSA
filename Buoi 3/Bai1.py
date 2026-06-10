def mot_luot_bubble_sort(a):
    
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]

    return a

a = [5, 1, 4, 2, 8]

print("Mảng ban đầu:", a)
print("Mảng sau 1 lượt Bubble Sort:", mot_luot_bubble_sort(a))