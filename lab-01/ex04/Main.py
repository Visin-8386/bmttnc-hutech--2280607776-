from QuanLySinhVien import QuanLySinhVien

def menu():
    print("\n===== QUAN LY SINH VIEN =====")
    print("1. Them sinh vien")
    print("2. Cap nhat thong tin sinh vien")
    print("3. Xoa sinh vien")
    print("4. Tim kiem sinh vien theo ID")
    print("5. Tim kiem sinh vien theo ten")
    print("6. Sap xep theo ID")
    print("7. Sap xep theo ten")
    print("8. Sap xep theo diem TB")
    print("9. Hien thi danh sach sinh vien")
    print("0. Thoat")

def main():
    qlsv = QuanLySinhVien()
    while True:
        menu()
        choice = input("Chon chuc nang: ")
        if choice == '1':
            qlsv.nhapSinhVien()
        elif choice == '2':
            try:
                id_sv = int(input("Nhap ID sinh vien can cap nhat: "))
                qlsv.updateSinhVien(id_sv)
            except ValueError:
                print("ID khong hop le!")
        elif choice == '3':
            try:
                id_sv = int(input("Nhap ID sinh vien can xoa: "))
                if qlsv.deleteById(id_sv):
                    print("Da xoa sinh vien co ID =", id_sv)
                else:
                    print("Khong tim thay sinh vien!")
            except ValueError:
                print("ID khong hop le!")
        elif choice == '4':
            try:
                id_sv = int(input("Nhap ID sinh vien can tim: "))
                sv = qlsv.findByID(id_sv)
                if sv:
                    qlsv.showSinhVien([sv])
                else:
                    print("Khong tim thay sinh vien!")
            except ValueError:
                print("ID khong hop le!")
        elif choice == '5':
            keyword = input("Nhap ten sinh vien can tim: ")
            listSV = qlsv.findByName(keyword)
            if listSV:
                qlsv.showSinhVien(listSV)
            else:
                print("Khong tim thay sinh vien!")
        elif choice == '6':
            qlsv.sortByID()
            print("Da sap xep theo ID!")
        elif choice == '7':
            qlsv.sortByName()
            print("Da sap xep theo ten!")
        elif choice == '8':
            qlsv.sortByDiemTB()
            print("Da sap xep theo diem TB!")
        elif choice == '9':
            qlsv.showSinhVien(qlsv.getListSinhVien())
        elif choice == '0':
            print("Tam biet!")
            break
        else:
            print("Vui long chon dung chuc nang!")

if __name__ == "__main__":
    main()
