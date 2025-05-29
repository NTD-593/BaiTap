don_vi = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
chuc = ["linh", "mười", "hai mươi", "ba mươi", "bốn mươi", "năm mươi", 
        "sáu mươi", "bảy mươi", "tám mươi", "chín mươi"]

while True:
    try:
        so = int(input("Nhập số có 3 chữ số (100-999): "))
        if 100 <= so <= 999:
            break
        else:
            print("Vui lòng nhập số có đúng 3 chữ số!")
    except ValueError:
        print("Vui lòng nhập số hợp lệ!")

hang_tram = so // 100
hang_chuc = (so % 100) // 10
hang_don_vi = so % 10

ket_qua = ""

if hang_tram > 0:
    ket_qua += don_vi[hang_tram] + " trăm "

if hang_chuc == 0:
    if hang_don_vi > 0:
        if hang_tram > 0:  
            ket_qua += "linh "
        ket_qua += don_vi[hang_don_vi]
else:
    ket_qua += chuc[hang_chuc] + " "
    if hang_don_vi > 0:
        if hang_chuc == 1:  
            ket_qua += don_vi[hang_don_vi]
        else:  
            if hang_don_vi == 1: 
                ket_qua += "mốt"
            elif hang_don_vi == 5:
                ket_qua += "lăm"
            else:
                ket_qua += don_vi[hang_don_vi]


print(f"Kết quả: {ket_qua}")