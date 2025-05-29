chuoi =input("Nhập chuỗi: ")
so = ()
for ky_tu in chuoi:
    if ky_tu>="0" and ky_tu<="9":
        so += (int(ky_tu),)

if so:
    print("Các số: ", so)
else:
    print("Ko có số nào !")