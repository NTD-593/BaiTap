ho_ten = input("Nhập họ và tên: ") 

cac_tu = ho_ten.split()

ho = ' '.join(cac_tu[:-1])
ten = cac_tu[-1]

print("Họ: ", ho)
print("Tên: ", ten)
