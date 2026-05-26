 #Bài 9. Tìm tất cả vị trí

def tim_tat_ca(a, x):
    kq = []

    for i in range(len(a)):
        if a[i] == x:
            kq.append(i)

    return kq

a = [4, 1, 4, 9, 4]
x = int(input("Nhap x: "))
print("Cac vi tri:", tim_tat_ca(a, x))