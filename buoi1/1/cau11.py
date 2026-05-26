#Bài 11. Tìm giá trị lớn nhất

def tim_max(a):
    maxx = a[0]

    for i in a:
        if i > maxx:
            maxx = i

    return maxx
a =[7, 3, 9, 12, 5, 8, 1]
print("Gia tri lon nhat:", tim_max(a))