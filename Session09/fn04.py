# Hàm với tham số có độ dài biến đổi
"""
Hàm có tham số với độ dài thay đổi 
Tham số thay đổi là một tham số đặc biệt
Khi gọi hàm có thể truyền 0,1 hoặc nhiều giá trị tương ứng với tham số của hàm
"""


def sum(a, b, *lst):

    res = a+b
    for x in lst:
        res = res + x

    return res


# /==End sum
tong = sum(10, 20, 30, 40, 50, 50)
print(tong)

# ví dụ


def tinhTong(*listNum):
    tong = 0
    for x in listNum:
        tong = tong+x
    print(tong)
# /==End tinhTong

tinhTong(10,20,30,40)
