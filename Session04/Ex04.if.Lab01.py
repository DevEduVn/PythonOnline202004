# Giải phương trình bậc nhất: ax+b=0
"""
	- Nhập hệ số
	- Thực hiện giải phương trình
	Nếu a == 0 
		Xét b; 
		nếu b==0 => phương trình có vô số nghiệm
		nếu b!=0=> phương trình vô nghiệm
	ngược lại; nếu a!=0
		=> nghiệm phương trình x =-b/a
"""
# Nhập
a = float(input("Nhập hệ số a="))
b = float(input("Nhập hệ số b="))
# Giải phương trình
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print(a, "x+", b, "=0 có nghiệm x=", x)
# =========
# if trên hàng
print("\n")
print("a=", a) if a > b else print("b=", b)
# ex: in ra số min của a, b
print("min = ", a) if a < b else print("min=", b)

# max(a,b)
print("max=", a) if a > b else print("max = ", b)

# if trên hàng với 3 điều kiện
print("a=", a) if a > b else print("a=b") if a == b else print("b=", b)
"""
if a > b:
    print("a=",a)
elif a == b:
    print("a=b")
else:
    print("b=",b)
"""
