"""
	- Cho một mảng các số nguyên
	- in ra các số nguyên tố
	- tính tổng các số nguyên tố

"""
lstNum = [10, 6, 9, 2, 3, 5, 13, 19, 17, 20]

# hàm kiểm tra số nguyên tố


def checkNT(a):
    if a <= 2:
        return True
    else:
        for x in range(2, a//2 + 1):
            if a % x == 0:
                return False
        return True
# /==End checkNT

# Hàm tính tổng các số nguyên tố


def tongNT(lst):
    tong = 0
    for x in lst:
        if checkNT(x) == True:
            tong = tong + x
    return tong
# /==End tongNT


# main
print("Danh sách dãy số nguyên ban đầu")
print(lstNum)
print("Các số nguyên tố")
for x in lstNum:
    if checkNT(x) == True:
        print(x, end=";")
t = tongNT(lstNum)
print("\n Tổng ", t)
