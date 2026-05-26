#Bài 18. Tìm kiếm trên ma trận 2 chiều

def tim_trong_ma_tran(mt, x):
    for i in range(len(mt)):
        for j in range(len(mt[i])):
            if mt[i][j] == x:
                return i, j

    return -1, -1


mt = [
    [5, 8, 1],
    [3, 9, 7],
    [2, 6, 4]
]

x = int(input("Nhap x: "))

dong, cot = tim_trong_ma_tran(mt, x)

if dong != -1:
    print("Tim thay tai:", (dong, cot))
else:
    print("Khong tim thay")
