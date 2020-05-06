# Mô tả hàm với tham số mặc định


def showInfo(name, gender="Male", phone="0978611889"):
    print("Xin chào:", name)
    print("Giới tính:", gender)
    print("Điện thoại:", phone)
# /==end showInfo


# Gọi hàm và không truyền giá trị cho các tham số mặc định
showInfo("Chung Trịnh")
# Gọi hàm với giá trị của các tham số đầy đủ
showInfo("Donal Trump", "Famale", "123123123123")

# showInfo()  # Error
showInfo("")

# ví dụ: định nghĩa một hàm không đúng quy tăc
"""
	- Tham số có giá trị mặc định và đặt sau tham số bắt buộc

def show(name="Dev ", address):
    print(name)
    print(address)
# /==end show
"""
