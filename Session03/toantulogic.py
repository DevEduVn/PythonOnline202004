"""
	and => kết hợp và [ 3>2 and 2<1 => false]
	or => kết hợp hoặc [ 3>2 or 2<1 => true]
	not => phủ định	 [ not(3>2 and 2<1) => true]
"""
x = input("Nhập x=")  # Nhận giá trị là một chuỗi
y = input("Nhập y=")
print("x=", x)
print("y=", y)
print("==========Thực hiện các phép toán logic")
x = int(x)
y = int(y)
z = x > y and y > 10
print(x, ">", y, " and ", y, ">10 =>", z)

z = x > y or y > 10
print(x, ">", y, " or ", y, ">10 =>", z)

z = not(x > y or y > 10)
print("not(", x, ">", y, " or ", y, ">10) =>", z)

"""
T ~ true
F ~ false

T and T => true
T and F => false
T or T => true
T or F => true
F and F => false

not(T) => false
not (F) => true

c/c++ / C# / java / javascript
and ~ &&
or ~ ||
not ~ !

"""
# Toán tử Identity: is / is not
a = 20
b = 20
if a is b:
    print(a, " is ", b, " => có cùng identity")
else:
    print(a, " is ", b, " => không có cùng identity")

# is not
if a is not b:
    print(a, " is not ", b, " => có cùng identity")
else:
    print(a, " is not ", b, " => không có cùng identity")

c = a is b
print(c)
c = a is not b
print(c)