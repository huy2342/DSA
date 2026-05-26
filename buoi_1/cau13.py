# Bài 13. Tìm kiếm trên chuỗi

def tim_ten(ds, ten):
    for i in range(len(ds)):
        if ds[i].lower() == ten.lower():
            return i
    return -1

ds = ["An", "Binh", "Chau"]

ten = input("Nhap ten can tim: ")

kq = tim_ten(ds, ten)

if kq != -1:
    print("Tim thay tai vi tri", kq)
else:
    print("Khong tim thay")