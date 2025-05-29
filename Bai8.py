chuoi = input("Nhập chuỗi: ")

ket_qua = ""
for i in range(len(chuoi)):
    if i % 2 == 0:  
        ket_qua += chuoi[i].upper()
    else: 
        ket_qua += chuoi[i].lower()

print("Chuỗi sau khi đổi:",ket_qua)