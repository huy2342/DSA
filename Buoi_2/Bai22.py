def find_median(a, b):
    if len(a) > len(b):
        a, b = b, a

    m = len(a)
    n = len(b)

    left = 0
    right = m

    while left <= right:
        i = (left + right) // 2
        j = (m + n + 1) // 2 - i

        maxLeftA = float('-inf') if i == 0 else a[i - 1]
        minRightA = float('inf') if i == m else a[i]

        maxLeftB = float('-inf') if j == 0 else b[j - 1]
        minRightB = float('inf') if j == n else b[j]

        if maxLeftA <= minRightB and maxLeftB <= minRightA:
            if (m + n) % 2 == 0:
                return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
            else:
                return max(maxLeftA, maxLeftB)

        elif maxLeftA > minRightB:
            right = i - 1
        else:
            left = i + 1

a = [1,2]
b = [3,4]

print(find_median(a, b))