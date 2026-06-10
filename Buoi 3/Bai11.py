def sap_xep_gia_tri_tuyet_doi(a):
    n = len(a)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if abs(a[j] > abs (a[j + 1])):
                a[j], a[j +1] = a[j + 1], a[j]
                
    return a

a = [-3, 1, -2, 2]
print("Mảng ban đâu: ", a)
print("Mảng sau khi sắp xếp theo trị tuyệt đối: ", sap_xep_gia_tri_tuyet_doi(a))