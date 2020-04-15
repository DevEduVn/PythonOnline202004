"""
	Nhập vào điểm toán, điểm văn
	Tính trung bình avg= (toan+van)/2
	Xếp loại:
		avg<5 => Yếu
		5<=avg<6 => Trung bình
		6<= avg < 7 => Khá
		7<= avg <8.5 => Giỏi
		8.6< avg <10 => Xuất sắc
	if...elif .... => 5'
"""
# Nhập
toan = float(input("Nhập điểm toán:"))
van = float(input("Nhập điểm văn:"))
# Tính điểm trung bình
avg = (toan+van)/2
# Xếp loại
if avg < 5:
    print(avg, " kém")
elif avg < 6:
    print(avg, " trung bình")
elif(avg < 7):
    print(avg, " khá")
elif(avg < 8.5):
    print(avg, " giỏi")
else:
    print(avg, " Xuất sắc")
# ====
