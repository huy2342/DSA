def can_allocate(pages, students, limit):
    count = 1
    total = 0

    for p in pages:
        if total + p > limit:
            count += 1
            total = 0

        total += p

    return count <= students

def book_allocation(pages, students):
    left = max(pages)
    right = sum(pages)
    ans = right

    while left <= right:
        mid = (left + right) // 2

        if can_allocate(pages, students, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

pages = [12,34,67,90]
students = 2

print(book_allocation(pages, students))