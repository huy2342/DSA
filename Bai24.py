def required_stations(stations, dist):
    count = 0

    for i in range(1, len(stations)):
        gap = stations[i] - stations[i - 1]
        count += int(gap / dist)

        if gap % dist == 0:
            count -= 1

    return count

def minimize_distance(stations, k):
    left = 0
    right = stations[-1] - stations[0]

    while right - left > 1e-6:
        mid = (left + right) / 2

        if required_stations(stations, mid) > k:
            left = mid
        else:
            right = mid

    return right

stations = [1,2,3,4,5,6,7,8,9,10]
k = 9

print(round(minimize_distance(stations, k), 6))