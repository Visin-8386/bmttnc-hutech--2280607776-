def kiem_tra_so_ngto(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

try:
    number = int(input("Nhập vào số cần kiểm tra: "))
    if kiem_tra_so_ngto(number):
        print(number, "là số nguyên tố")
    else:
        print(number, "không là số nguyên tố")
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ!")