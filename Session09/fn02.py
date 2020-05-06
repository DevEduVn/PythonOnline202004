# Hàm có giá trị trả về; (Sử dụng lệnh return trong hàm)
# Định nghĩa


def getGreeting(name):
    if not name:
        return "Hello everybody!"
    else:
        return "Hello " + name


# /==end def
# Gọi hàm => gán giá trị của hàm cho biến, hoặc thực hiện các thao tác trên giá trị đó
res = getGreeting("")
print(res)

print(getGreeting("Chung Trịnh"))

"""
	ví dụ:
	- viết hàm thực hiện cộng 2 số, hàm trả về giá trị tổng của 2 số
"""


def add(a, b):
    return a+b


# Gọi thực hiện hàm
print("Cộng: 10+20=", add(10, 20))

# Hàm có tham số bắt buộc
# c = add(10)  # error
c = add(10, 20)
print(c)


# Hàm không có tham số
def hello():
    print("Xin chào python")
    print("Toi là tôi")


# gọi hàm
hello()
