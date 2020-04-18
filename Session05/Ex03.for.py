# for demo
# in ra số nguyên <=n
n = int(input("Nhập n="))
for x in range(n):
    print(x)
# /==end for
# https://pynative.com/python-range-function/
# in ra các số nguyên từ n=> m
m = int(input("Nhập m="))
for x in range(n, m):
    print(x)
# /==end for

# range(start, end, step)
print("range(2,20,5):")
s = ""
for x in range(2, 20, 5):
    s = s + str(x) + "; "
print(s)
# in trên 1 dòng
for x in range(2, 20, 5):
    print(x, end=', ')

# lặp trong một mảng
names = ["Devmaster", "Academy"]
for item in names:
	print(item, end=' ')

# Mảng ký tự
names = "Devmaster Academy"
for ch in names:
	print(ch)

"""
Xử lý với for:
	1. kiểm tra số n có phải là số nguyên tố không?
	2. Kiểm tra số n có phải là số chính phương không?
	3. Tính tổng các số nguyên tố <=n
	4. Nhập vào 1 mảng số nguyên gồm n phần tử
		=> In ra mảng
		=> Tính tổng các phần tử
"""