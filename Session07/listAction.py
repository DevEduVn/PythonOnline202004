# Tương tác với list
lstNum = [2029, 1900, 2000, 1989, 1999, 2029, 1950, 1234]
# Các hàm thường dùng
# Hàm len => độ dài của list
print(lstNum, end=" = ")
print(len(lstNum))
# Hàm max => Lấy giá trị lớn nhất
print("Max = ", max(lstNum))

# Hàm min => Lấy giá trị nhỏ nhất
print("Min = ", min(lstNum))

# Các phương thức thường dùng:
# append => thêm vào cuối danh sách
lstNum.append(5000)
print(lstNum)
# count => Trả về số lần xuất hiện của phần tử trong danh sách
print(lstNum.count(2029))
# extend

# index
print(lstNum.index(2029))
# insert
lstNum.insert(1, 3000)
print(lstNum)
# pop => Loại bỏ phần tử trong danh sach
lstNum.pop()  # Loại bỏ phần tử cuối
print(lstNum)
lstNum.pop(1)  # Loại bỏ phần tử tại vị trí 1
print(lstNum)

# remove

# reverse
lstNum.reverse()
print(lstNum)
# sort
print("Sort:")
lstNum.sort()
lstNum.reverse()
print(lstNum)

print("HA "*3)
