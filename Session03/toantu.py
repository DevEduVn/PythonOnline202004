# Các toán tử số học: +; -; *; / ; %; //; **
# Nhập giá trị cho 2 biến x, y => thực hiện các phép tương ứng
x = input("Nhập x=")  # Nhận giá trị là một chuỗi
y = input("Nhập y=")
print("x=", x)
print("y=", y)
print("==========Thực hiện các phép toán số học")
x = int(x)
y = int(y)
z = x+y
print("{0} + {1} = {2}".format(x, y, z))
z = x-y
print("{0} - {1} = {2}".format(x, y, z))
z = x*y
print("{0} * {1} = {2}".format(x, y, z))
z = x/y
print("{0} / {1} = {2}".format(x, y, z))
z = x % y
print("{0} % {1} = {2}".format(x, y, z))
z = x//y
print("{0} // {1} = {2}".format(x, y, z))
z = x**y
print("{0} ^ {1} = {2}".format(x, y, x**y))

# Toán tử gán
print("{0} = {1}".format(x, x))
z = x
x += 5  # x = x + 10 => x =10 +10
print("x +=5 => x=", x)
x -= 10
print("x -=10 => x=", x)  # x = 5
x *= 5
print("x *=5 => x=", x)  # x=25
x /= 5
print("x /=5 => x=", x)  # x=5
x %= 3
print("x /=3 => x=", x)  # x=2
x //= 2
print("x //=2 => x=", x)  # x=1
z **= 2
print("z **=2 => z=", z)  # z =100
