 #Bài 8. Đếm số lần xuất hiện
def dem_xuat_hien(a, x):
    dem = 0
    for i in a:
        if i == x:
            dem += 1
    return dem
a =[2, 5, 2, 7, 2]
x =int(input("Nhap x: "))
print("So lan xuat hien:", dem_xuat_hien(a, x))