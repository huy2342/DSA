def so_luot_it_nhat(ban_dau, hien_tai):
    tam = ban_dau[:]
    n = len(tam)

    for luot in range(1, n):

        for j in range(n - luot):
            if tam[j] > tam[j + 1]:
                tam[j], tam[j + 1] = tam[j + 1], tam[j]

        if tam == hien_tai:
            return luot

    return -1

ban_dau = [4, 3, 2, 1]
hien_tai = [3, 2, 1, 4]

print("Mảng ban đầu:", ban_dau)
print("Mảng hiện tại:", hien_tai)
print("Số lượt ít nhất đã thực hiện:", so_luot_it_nhat(ban_dau, hien_tai))