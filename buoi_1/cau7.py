#Bài 7 Kiểm tra tồn tại

def ton_tai(a, x):
    for i in a:
        if i == x:
            return True
    return False

a =[7, 3, 9, 12, 5, 8, 1]
x= int(input("Nhap x: "))
print(ton_tai(a, x))
