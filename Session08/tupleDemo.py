# Tuple => Là một danh sách bất biến
# Khai báo: sử dụng cặp dấu()
tup1 = (1900, 1991, 1995)
print(tup1)
# thêm => Vì nó là bất biến nên không thể thêm sau khi đã định nghĩa
# Xuất danh sách dựa vào tập hợp, chỉ số
for item in tup1:
    print(item)

print("Xuất danh sách theo chỉ số")
for x in range(0, len(tup1)):
    print(tup1[x])

# Sử dụng các phép toán với tuple => +; *; in
tup2 = ("One", "Two", "Three")
print("Phép +")
tup3 = tup1+tup2
print(tup3)
# *
tup3 = tup1*3
print(tup3)
# in
flag = 1995 in tup1
print(flag)
print(1996 in tup1)

# một số hàm với tuple
print("Max:", max(tup1))
print("Min:", min(tup1))
print("Len:", len(tup1))

# convert
lst = ["Một", "Hai", "Ba"]
print(lst)
tup4 = tuple(lst)
print(tup4)

lst.append("Bốn")
print(lst)
print(tup4)

#
tup1 = (1900, 1991, 1992, 1900, 1992, 1995)
print(tup1.count(1900))

lst = [1900, 1991, 1992, 1900, 1992, 1992, 1996]
# Đếm xem trong danh sách có bao nhiêu phần tử 1992
print(tuple(lst).count(1992))

# index => tìm kiếm trả về vị trí đầu tiên tìm thấy
tup4 = tuple(lst)
print(tup4.index(1992, 3, 5))
