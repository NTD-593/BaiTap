print("Nhập Tên: ")
ten_nhap = input()
ten_thuong = ten_nhap.lower()

tu_dau = True
ket_qua = ""
for ky_tu in ten_thuong:
    if ky_tu == " ":
        tu_dau = True
        ket_qua += " "
    else:
        if tu_dau:
            ket_qua += ky_tu.upper()
            tu_dau = False
        else:
            ket_qua += ky_tu
print("Tên đã chuẩn hóa: ", ket_qua)