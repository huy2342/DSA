def tron_va_dem(trai, phai):
    ket_qua = []
    i = j = 0
    nghich_the = 0

    while i < len(trai) and j < len(phai):
        if trai[i] <= phai[j]:
            ket_qua.append(trai[i])
            i += 1
        else:
            ket_qua.append(phai[j])
            nghich_the += len(trai) - i
            j += 1

    ket_qua.extend(trai[i:])
    ket_qua.extend(phai[j:])

    return ket_qua, nghich_the


def dem_nghich_the_nhanh(a):
    if len(a) <= 1:
        return a, 0

    giua = len(a) // 2

    trai, x = dem_nghich_the_nhanh(a[:giua])
    phai, y = dem_nghich_the_nhanh(a[giua:])

    ket_qua, z = tron_va_dem(trai, phai)

    return ket_qua, x + y + z


a = [2, 3, 8, 6, 1]

so_swap = dem_nghich_the_nhanh(a)

print("Mảng ban đầu:", a)
print("Số swap của Bubble Sort:", so_swap)