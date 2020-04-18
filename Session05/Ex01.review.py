# if, if...else; if...elif ... else; if... if..elif...else
# Nhập vào thang, nam => in ra số ngày
"""
	thang=4
	nam=2020

	=> số ngày = 30
"""
thang = int(input("Thang:"))
nam = int(input("Nam:"))
soNgay = 0
# Xử lý
"""
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    soNgay = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    soNgay = 30
elif thang == 2:
    if nam % 4 == 0 and nam % 100 != 0:
        soNgay = 29
    else:
        soNgay = 28
else:
	print("Bạn nhập sai tháng")
"""

# /==begin
if thang in {1, 3, 5, 7, 8, 10, 12}:
    soNgay = 31
elif thang in {4, 6, 9, 11}:
    soNgay = 30
elif (thang == 2) and (nam % 4 ==0 and nam % 100 !=0):
    soNgay=29
elif thang == 2 and (nam % 4 ==0 and nam % 100 ==0):
	soNgay=28
else:
    print("Bạn nhập sai tháng [1-12]")
if soNgay > 0:
    print("Tháng ", thang, " năm ", nam, " có ", soNgay, " ngày!")
# /==end
