# Python không phân biệt kiểu dữ liệu khi khai báo (dynamic)
# int x;  trong c, java,.. ;
# Khai báo biến phải gán giá trị cho biến => xác định được kiểu dl
# dùng hàm type để kiểm tra kiểu
x = 10  # int
y = 10.1  # float
z = 2j  # complex
print(type(x))
print(type(y))
print(type(z))

# float
x = 10.2
y = 12E4
z = 12.3e100
print(x, y, z)
# int (biến, gán giá trị, in giá trị, in ra kiểu 1 biến)
x = 123
print(x)
print(type(x))

# Complex -> Kiểu số phức
# Khai báo biến kiểu số phức, gán giá trị, in ra phần thực, phần ảo, kiểu
x = 123 + 234j
print(x)
print(type(x))
# in ra phần thực
print("Phần thực:", x.real)
# in ra phần ảo
print("Phần ảo:", x.imag)

# Ép kiểu trong python (Casting)
# Trong một số trường hợp ta thường phải chuyển đổi kiểu dữ liệu khi tính toán
# Ép kiểu sang kiển int
x = int(100)
y = int(123.12)
z = int("1234")
# a = int("123abc") -> ERROR
print(x, y, z)

x = 20
y = 8
z = x/y
print(x, y, z)

# Ép kiểu sang kiểu float
print(float(123))
# ví dụ: khai báo biến kiểu số nguyên => ép sang kiểu số thực; in ra kiểu tương ứng
x = 123
y = float(x)
print(x, y)
print(type(x), type(y))

# Ép sang kiểu chuỗi
x = str("str1")
y = str(2020)
z = str(4.0)
print(x, y, z)
a = y+z
print(a)
a = x+y+z
print(a)
print(type(x))

# Kiểu chuỗi, xử lý chuỗi cơ bản trong python
# Bắt đầu bằng ' hoặc "
str1 = "Hello"
str2 = 'World'
print(str1, str2)

# Bạn muôn in ra chuỗi "Hello World" hoặc 'Hello World'
print("Hello world")
print('"Hello world"')
print("'Hello world'")
# Viết chuỗi trên nhiều dòng
# Hello
# World
str1 = """ Hello
			world
		"""
print(str1)
# Chuỗi bản chất là một mảng ký tự
# => Ta có thể truy xuất đến từng ký tự thông mảng ký tự
# Mảng ký tự có chỉ số bắt đầu từ 0

str1 = "Chung Trinhj Van"
print(str1)
print(str1[1])

# Tách chuỗi con
print(str1[6:12])
str1 = "     Chung Trinhj Van "
print(str1)

# Cắt khoảng trắng
print(str1.strip())

# Độ dài của chuỗi => hàm len
print(len(str1))
str1 = str1.strip()
print(len(str1))

# chuyển đổi chữ hoa, chữ thường
str1 = str1.upper()  # chuyển thành chữ HOA
print(str1)
str1 = str1.lower()  # chuyển thành chữ thường

# Thay thế ký tự, chuỗi ký tự
# Thay ký tự j bằng rỗng
print(str1)
str1 = str1.replace('j', '')
print(str1)
str1 = str1.replace('trinh', '---')
print(str1)

# Tách chuỗi thành mảng các từ, hoặc mảng các ký tự
str1 = "Chung Trịnh Văn"
print(str1)
# ==> sử dụng hàm split để tách
print(str1.split(" "))
arr = str1.split(' ')
print(arr)  # mảng các phần tử
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[2])

print(arr[0][0])

# Nỗi chuỗi
print('Enter you name:')
name=input()
print("Welcome ," + name)
