def can_eat(piles, h, speed):
    hours = 0 
    
    for bananas in piles:
        hours += (bananas + speed - 1) // speed
    
    return hours <= h

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    ans = right
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_eat(piles, mid, h):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return ans

piles = [3, 6, 7, 11]
h = 8

print(min_eating_speed(piles, h))