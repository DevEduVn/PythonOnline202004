# In ra số có 2 chữ số mà tổng của chúng là số chẵn
for x in range(10, 100):
    hc = x//10
    dv = x % 10
    if (hc + dv) % 2 == 0:
        print(x, end="; ")
# /== End
print("\n")
for x in range(1, 10):
    for y in range(0, 10):
        if (x + y) % 2 == 0:
            num = x*10 + y
            print(num, end="; ")
# /==End
