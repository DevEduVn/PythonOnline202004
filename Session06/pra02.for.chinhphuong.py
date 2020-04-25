"""
# 3. kiểm tra số n có phải là số chính phương không?
n = int(input("Nhập n:"))
# xử lý
flag = False  # Giả định n không là số chính phương
for x in range(2, int(n/2)+1):
    if (x**2 == n):
        flag = True
        break
    # kết thức for
if flag == True:
    print(n, " là số chính phương")
else:
    print(n, " không phải là số chính phương")
# /== end
"""
# 4. In ra các số chính phương <=n, tính tổng
n = int(input("Nhập n:"))
print("Dãy các số chính phương <=:", n)
tong = 0
for i in range(1, n+1):
    flag = False  # Giả định i là số chính phương
    for j in range(2, int(i/2) + 1):
        if j**2 == i:
            flag = True
            break
    # / end for check j->
    if flag == True:
        print(i, end="; ")
        tong = tong + i
print("\nTổng:", tong)
# /=End for i: 1=>n
