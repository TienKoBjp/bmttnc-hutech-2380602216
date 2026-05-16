import re

chuoi = "-100#^sdfkj8902w3ir021@swf-20"
cac_so = re.findall(r'-?\d+', chuoi)

tong_duong = sum(int(so) for so in cac_so if int(so) > 0)
tong_am = sum(int(so) for so in cac_so if int(so) < 0)

print(f"Kết quả: Giá trị dương: {tong_duong}. Giá trị âm: {tong_am}.")