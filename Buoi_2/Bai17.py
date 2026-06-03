def can_ship(weights, D, capacity):
    days = 1
    current = 0

    for w in weights:
        if current + w > capacity:
            days += 1
            current = 0

        current += w

    return days <= D

def ship_capacity(weights, D):
    left = max(weights)
    right = sum(weights)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if can_ship(weights, D, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

weights = [1,2,3,4,5,6,7,8,9,10]
D = 5

print(ship_capacity(weights, D))