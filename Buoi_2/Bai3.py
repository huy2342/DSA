def first_position(a, x):
    left = 0
    right = len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            ans = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans

a = [1, 2, 2, 2, 3]
x = 2

print(first_position(a, x))