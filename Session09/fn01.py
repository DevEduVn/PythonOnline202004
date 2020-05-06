# Khái niệm về hàm python
"""
	-> Định nghĩa hàm:
		=> Hàm có tham số, tham số bắt buộc, tham số tùy chọn,..
	-> Sử dụng hàm: 
		=> Gọi hàm: có giá trị trả về
		=> Gọi hàm: không có giá trị trả về
"""
# Định nghĩa hàm


def sayHello(name):

    # Kiểm tra tham số name nếu không có giá trị
    if not name:
        print("Xin chào tất cả mọi người")
    else:
        # Biến name có giá trị
        print("Xin chào,", name)
# /==End function sayHello


# Sử dụng hàm (gọi thực hàm)
sayHello("")  # Gọi hàm mà không truyền giá trị cho đối số
sayHello("Donal Trump")
