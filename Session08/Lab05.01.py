"""
1.	Viết chương trình thực hiện các công việc sau
a.	Tạo 1 list rỗng
b.	Nhập 1 số nguyên dương n
c.	Nhập n phần tử vào danh sách
d.	Hiển thị danh sách vừa nhập
e.	Nhập một giá trị; tìm kiếm xem trong danh sách có giá trị nào bằng với giá trị người dùng nhập không? Nếu tìm thấy in ra màn hình; ngược lại thông báo không tìm thấy.
"""
lst = []
n = int(input("Nhập n="))
# Nhập danh sách các phần tử
for x in range(0, n):
    print("Nhập phần tử thư ", x)
    temp = int(input())
    lst.append(temp)

# In ra danh sách
print(lst)

# Tìm kiếm
keyword = int(input("Nhập giá trị tìm:"))
flag = False
for x in range(0, n):
    if(lst[x] == keyword):
        flag = True
        print(x, "=>", lst[x])
if(flag == False):
    print("Không tìm thấy")
# /==End
