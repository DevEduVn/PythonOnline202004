# Amstrong: abc = a^3 + b^3 +c^3
"""
a = abc // 100
c = abc % 10
b = (abc % 100) // 10

"""

print("Dãy số amstrong:")
for x in range(100, 1000):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if a**3 + b**3 + c**3 == x:
        print(x, end="; ")
# //==End
print("\n While")
x = 100
while(x <= 999):
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if a**3 + b**3 + c**3 == x:
        print(x, end="; ")
    x = x + 1
# //==End
