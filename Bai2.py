print("Nhập chuỗi: ")
chuoi = input()

tudaonguoc = chuoi.split( )[::-1]
ket_qua = ' '.join(tudaonguoc)

print("Kết quả:", ket_qua)