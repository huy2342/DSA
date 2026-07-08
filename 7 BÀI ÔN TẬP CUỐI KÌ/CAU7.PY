A = [3, 4, 7, 2, -3, 1, 4, 2]
S = 7

tong = 0
dem = 0
mp = {0: 1}

for x in A:
    tong += x

    if tong - S in mp:
        dem += mp[tong - S]

    if tong in mp:
        mp[tong] += 1
    else:
        mp[tong] = 1

print(dem)