def can_place(baskets, m, distance):
    count = 1
    last = baskets[0]

    for i in range(1, len(baskets)):
        if baskets[i] - last >= distance:
            count += 1
            last = baskets[i]

    return count >= m

def magnetic_force(baskets, m):
    baskets.sort()

    left = 1
    right = baskets[-1] - baskets[0]
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place(baskets, m, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

baskets = [1,2,3,4,7]
m = 3

print(magnetic_force(baskets, m))