print("Nhap cac dong van ban (Nhap 'done' de ket thuc')")
lines = []
while True:
    LINE = input()
    if LINE.lower() == 'done':
        break
    lines.append(LINE)
print("\nCac dong da nhap sau khi chuyen thanh chu in hoa")
for line in lines:
    print(line.upper())