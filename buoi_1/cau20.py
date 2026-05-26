#Bài 20. Quản lý danh bạ đơn giản

danh_ba = {
    "An": "0901234567",
    "Binh": "0912345678",
    "Chau": "0909999999"
}

while True:
    print("\n===== MENU =====")
    print("1. Tim theo ten")
    print("2. Tim theo so dien thoai")
    print("3. Dem so dien thoai bat dau bang 090")
    print("0. Thoat")

    chon = input("Nhap lua chon: ")

    if chon == "1":
        ten = input("Nhap ten: ")

        if ten in danh_ba:
            print("So dien thoai:", danh_ba[ten])
        else:
            print("Khong tim thay")

    elif chon == "2":
        sdt = input("Nhap so dien thoai: ")

        tim_thay = False

        for ten in danh_ba:
            if danh_ba[ten] == sdt:
                print("Chu so huu:", ten)
                tim_thay = True
                break

        if not tim_thay:
            print("Khong tim thay")

    elif chon == "3":
        dem = 0

        for sdt in danh_ba.values():
            if sdt.startswith("090"):
                dem += 1

        print("Co", dem, "so dien thoai bat dau bang 090")

    elif chon == "0":
        print("Da thoat")
        break

    else:
        print("Lua chon khong hop le")