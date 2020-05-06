# Giải phương trình bậc 2: ax2+bx+c=0
import math


def giaiPTBacNhat(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô  nghiệm")
    else:
        x = -b/a
        print("Phương trình có nghiệm x=", x)
# /==End giaiPTBacNhat


def giaiPTBacHai(a, b, c):
    if(a == 0):
        giaiPTBacNhat(b, c)
    else:
        # tính delta
        delta = b*b - 4*a*c
        if delta < 0:
            print("Phương trình vô nghiệm")
        elif delta == 0:
            print("Phương trình có nghiệm kép x1=x2=", -b/a)
        else:
            x1 = (-b*b - math.sqrt(delta))/(2*a)
            x2 = (-b*b + math.sqrt(delta))/(2*a)
            print("x1=", x1)
            print("x2=", x2)
# /==End giaiPTBacHai


# Nhập các hệ số
a = float(input("Nhập a="))
b = float(input("Nhập b="))
c = float(input("Nhập c="))

giaiPTBacHai(a, b, c)
