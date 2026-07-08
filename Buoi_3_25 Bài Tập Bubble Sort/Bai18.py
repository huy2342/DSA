class Nut:
    
    def __init__(self, du_lieu):
        self.du_lieu = du_lieu
        self.ke_tiep = None


def bubble_sort_danh_sach_lien_ket(dau):
    if dau is None:
        return dau

    da_hoan_doi = True

    while da_hoan_doi:
        da_hoan_doi = False
        hien_tai = dau

        while hien_tai.ke_tiep:
            if hien_tai.du_lieu > hien_tai.ke_tiep.du_lieu:
                hien_tai.du_lieu, hien_tai.ke_tiep.du_lieu = \
                hien_tai.ke_tiep.du_lieu, hien_tai.du_lieu

                da_hoan_doi = True

            hien_tai = hien_tai.ke_tiep

    return dau


def in_danh_sach(dau):
   
    while dau:
        print(dau.du_lieu, end=" -> ")
        dau = dau.ke_tiep
    print("None")


a = Nut(1)
b = Nut(3)
c = Nut(2)

a.ke_tiep = b
b.ke_tiep = c

bubble_sort_danh_sach_lien_ket(a)

print("Danh sách liên kết sau khi sắp xếp:")
in_danh_sach(a)