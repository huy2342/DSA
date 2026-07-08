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

def last_position(a, x):
    left = 0
    right = len(a) - 1
    ans = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            ans = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return ans

def count_occurrences(a, x):
    first = first_position(a, x)

    if first == -1:
        return 0

    last = last_position(a, x)

    return last - first + 1

a = [1, 2, 2, 2, 3]
x = 2

print(count_occurrences(a, x))