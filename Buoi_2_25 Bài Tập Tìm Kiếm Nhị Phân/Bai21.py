def can_split(nums, k, limit):
    count = 1
    total = 0

    for num in nums:
        if total + num > limit:
            count += 1
            total = 0

        total += num

    return count <= k

def split_array(nums, k):
    left = max(nums)
    right = sum(nums)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if can_split(nums, k, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

nums = [7,2,5,10,8]
k = 2

print(split_array(nums, k))