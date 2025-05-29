chuoi = input("Nhập chuỗi: ")

dem = {}
for ky_tu in chuoi:
    if ky_tu in dem:
        dem[ky_tu] += 1
    else:
        dem[ky_tu] = 1

for ky_tu, so_lan in dem.items():
    print(ky_tu+":", so_lan)
