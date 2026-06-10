def sap_xep_hoc_sinh(ds):
    n = len(ds)

    for i in range(n - 1):
        for j in range(n - 1 - i):

            if ds[j][1] < ds[j + 1][1]:
                ds[j], ds[j + 1] = ds[j + 1], ds[j]

            elif ds[j][1] == ds[j + 1][1]:
                if ds[j][0] > ds[j + 1][0]:
                    ds[j], ds[j + 1] = ds[j + 1], ds[j]

    return ds

ds = [("An", 8), ("Ba", 9), ("Cu", 8)]

print("Danh sách học sinh ban đầu:", ds)
print("Danh sách sau khi sắp xếp:", sap_xep_hoc_sinh(ds))