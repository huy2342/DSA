#Bài 12. Min và Max trong một lần duyệt

def min_max(a):
    minn = a[0]
    maxx = a[0]

    vi_tri_min = 0
    vi_tri_max = 0

    for i in range(len(a)):
        if a[i] < minn:
            minn = a[i]
            vi_tri_min = i

        if a[i] > maxx:
            maxx = a[i]
            vi_tri_max = i
    print("Min =", minn, "tai vi tri", vi_tri_min)
    print("Max =", maxx, "tai vi tri", vi_tri_max)
a = [7, 3, 9, 12, 5, 8, 1]
min_max(a)