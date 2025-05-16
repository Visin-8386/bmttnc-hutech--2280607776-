def chia_het_cho5(so_nhi_phan):
    try:
        so_thap_phan = int(so_nhi_phan, 2)
        return so_thap_phan % 5 == 0
    except ValueError:
        return False

chuoi_so_nhi_phan = input("Nhập chuỗi số nhị phân (phân tách bởi dấu phẩy): ")

so_nhi_phan_list = [so.strip() for so in chuoi_so_nhi_phan.split(',') if so.strip()]

so_chia_het_cho5 = [so for so in so_nhi_phan_list if chia_het_cho5(so)]

if so_chia_het_cho5:
    ket_qua = ','.join(so_chia_het_cho5)
    print("Các số nhị phân chia hết cho 5 là:", ket_qua)
else:
    print("Không có số nhị phân nào chia hết cho 5 trong chuỗi đã nhập.")