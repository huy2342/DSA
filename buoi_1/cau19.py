 #Bài 19. Tìm kiếm theo khóa

ds = [
    {"ma_sv": "SV01", "ten": "An", "dtb": 8.5},
    {"ma_sv": "SV02", "ten": "Binh", "dtb": 7.8},
    {"ma_sv": "SV03", "ten": "Chau", "dtb": 9.1}
]

ma = input("Nhap ma sinh vien: ")

tim_thay = False

for sv in ds:
    if sv["ma_sv"] == ma:
        print("Ma SV:", sv["ma_sv"])
        print("Ten:", sv["ten"])
        print("DTB:", sv["dtb"])
        tim_thay = True
        break

if not tim_thay:
    print("Khong tim thay sinh vien")