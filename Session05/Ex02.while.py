# =============while
"""
while(conditon):
	statement - condition=true

ví dụ: 
- Nhập một nguyên n
- in ra các số nguyên <=n
- Tính tổng các số nguyên
"""
# Nhập số nguyên n
n = int(input("n="))
# Khai báo và khởi tạo biến lặp
i = 0
tong = 0  # khai báo và khởi tạo biến tổng
while(i <= n):
    print(i)
    tong += i
    i = i+1
# các lệnh ngoài vòng lặp
print("Tổng = ", tong)
# /==end
# Kiểm tra số n có phải là số nguyên tố không?
# => Số nguyên tố là số chỉ có ước là 1 và chính nó: 2,3,5,7,11,...
# process
# giả định n là số nguyên tố
flag = True
i = 2
while (i <= int(n/2)):
    if n % i == 0:
        flag = False
        break
    i = i+1
# kết thúc kiểm tra
if flag == True:
    print(n, " là số nguyên tố")
else:
    print(n, " không là số nguyên tố")
# Kiểm tra số n có phải là số chính phương hay không
# 4, 9 ,16, 25,.. -> Số có căn nguyên bậc 2
