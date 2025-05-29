chuoi = input("Nhập chuỗi: ")

ky_tu_nhieu_nhat = ''
so_lan_nhieu_nhat = 0

for ky_tu in chuoi:
    dem = chuoi.count(ky_tu)
    
    if dem > so_lan_nhieu_nhat:
        so_lan_nhieu_nhat = dem
        ky_tu_nhieu_nhat = ky_tu

print("ký tự:",ky_tu_nhieu_nhat)
print("số lần:",so_lan_nhieu_nhat)