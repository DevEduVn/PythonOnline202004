# Cấu trúc điều khiển if
# if đơn
# Syntax:
"""
	if condition:
		statement - block;

	Ví dụ:
	- Nhập vào số nguyên
	- Kiểm tra nếu >0 => in ra là số dương
"""
n = input("Nhập n=")
n = int(n)  # chuyển về số nguyên
if n > 0:
    print(n, "Là số dương.")
# ==============================1
# if đầy đủ
"""
	if condition:
		statement - condition=true
	else:
		statement - condition=false
	Ex: Nhập số n => kiểm tra xem n là dương hay số âm

"""
if n > 0:
    print(n, " là số dương.")
else:
    print(n, " là số âm.")
# ===========
# ex01: kiểm tra xem n là số chẵn hay số lẻ (n%2==0)
if n % 2 == 0:
    print(n, " là số chẵn")
else:
    print(n, " là số lẻ")
# ============
# if bậc thang
"""
	if condition:
		statement - condition=true
	elif condition 2:
		stetment..
	...
	else:
		statement => tất cả các điều kiện trong if đều sai
"""
# Kiểm tra n là số dương hay số âm hay bằng 0
if n > 0:
    print(n, " là số dương")
elif n == 0:
    print(n, " là số 0")
else:
    print(n, " là số âm")
# =============
# if lồng nhau
"""
	if condtion:
		statement
		if cond:
			statement
		else:
			statement
	else:
		if cond:
			statement
		elif cond1:
			...
		else:
			statment...
"""
