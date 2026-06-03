def can_place(stalls, cows, distance):
    count = 1
    last = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - last >= distance:
            count += 1
            last = stalls[i]

    return count >= cows

def aggressive_cows(stalls, cows):
    stalls.sort()

    left = 1
    right = stalls[-1] - stalls[0]
    ans = 0

    while left <= right:
        mid = (left + right) // 2

        if can_place(stalls, cows, mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    return ans

stalls = [1,2,4,8,9]
cows = 3

print(aggressive_cows(stalls, cows))