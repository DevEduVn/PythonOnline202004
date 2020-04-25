# List in python
"""
Python list có khả năng lưu trữ các kiểu dữ liệu khác nhau
Bạn có thể thay đổi phần tử trong list
Thứ tự trong List bắt đầu từ 0
Giá trị lưu trong List được phân cách bởi dấu phẩy
"""
# Khai báo một list các phần tử, sử dụng cặp dấu  []
lst = ["Táo", "Lê", "Đào", "Mận", "Quýt", "Mơ"]
# In
print(lst)

# Khai báo list hỗn hợp kiểu
lst1 = ["Táo", 10, "Lê", 20]
print(lst1)

# Duyệt mảng thông qua vòng lặp
for x in lst:
    print(x)
# //=End

# Truy cập thông qua chỉ số mảng (Chỉ số bắt đầu từ 0)
for i in range(0, len(lst)):
    print(lst[i])
# //=End

# Truy cập đến tập con trong danh sách => thông qua chỉ số
print(lst)
print(lst[1:4])  # Tập con có chỉ số 1,2,3

# Truy cập thông qua chỉ số âm
print(lst)
print("lst[-1]=>", lst[-1])
print("lst[-2]=>", lst[-2])
print("lst[-4:]=>", lst[-4:])
print("lst[-5:-3]=>", lst[-5:-3])
print("lst[-3:-1]=>", lst[-3:-1])


# Thay đổi giá trị của list thông qua chỉ số
years = [2001, 2002, 2005, 2008, 2009, 2010, 2018, 2019]
print(years)

years[0] = 2000  # Thay đổi giá trị trong list tại chỉ số 0
print(years)

# Thay đổi một đoạn
years[2:6] = [2010, 2015]
print(years)

# Thêm giá trị vào cuối danh sách
years.append(2020)
print(years)

# Thêm vào đầu danh sách 2 phần tử
# years[0] = [1998, 1999]
# print(years)

# Xóa
del (years[0])
print(years)

del years[0:2]
print(years)

years.remove(2019)
print(years)

years1 = [2020, 2030, 2040]
lstNew = years+years1
print(lstNew)

cuoi = ["Ha", "Ha", "Ha"]
print(cuoi)
cuoi = ["Ha"]
print(cuoi*3)
