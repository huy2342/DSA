 #Bài 10.Vị trí xuất hiện cuối cùng
def vi_tri_cuoi(a, x):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i
    return -1
a =[4, 1, 4, 9, 4]
x =int(input("Nhap x: "))
print("Vi tri cuoi:", vi_tri_cuoi(a, x))