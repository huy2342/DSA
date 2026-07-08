def sap_xep_chuoi_theo_do_dai(a):
    n = len(a)
    
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if len(a[j] > len(a[j + 1])):
                a[j], a[j + 1] = a[j + 1], a[j]
            
    return a

a = ["abc", "a", "ab"]

print("Danh sách chuỗi ban đầu:", a)
print("Danh sách chuỗi sau khi sắp xếp:", sap_xep_chuoi_theo_do_dai(a))