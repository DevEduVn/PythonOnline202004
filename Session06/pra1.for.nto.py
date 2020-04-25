# 1. kiểm tra số n có phải là số nguyên tố không?
"""
n = int(input("Nhập n:"))
# xử lý
flag = True  # Giả định n là số nguyên tố
for x in range(2, int(n/2)+1):
    if n % x == 0:
        flag = False
        break
    # kết thức for
if flag == True:
    print(n, " là số nguyên tố")
else:
    print(n, " không phải là số nguyên tố")
# /== end
"""

# 2. In ra các số nguyên tố <=n, tính tổng
n = int(input("Nhập n:"))
print("Dãy các số nguyên tố <=:", n)
tong = 0
for i in range(1, n+1):
    flag = True  # Giả định i là số nguyên tố
    for j in range(2, int(i/2) + 1):
        if i % j == 0:
            flag = False
            break
    # / end for check j->
    if flag == True:
        print(i, end="; ")
        tong = tong + i
print("\nTổng:", tong)
# /=End for i: 1=>n
