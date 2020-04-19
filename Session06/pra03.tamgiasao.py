# Sử dụng vòng lặp lồng nhau để in tam giá sao
"""
input n=5
output:
n=5
	* 
	* *
	* * *
	* * * *
	* * * * *
/=end
"""
# Hướng dẫn
"""
- Vòng for (i) lặp theo dòng từ 1 -> n
	- Vòng for (j) lặp theo cột 1-> i => In ra *
		-> In hết for trong, xuống dòng end='\n'
______________________________________________________________
"""
n = int(input("Nhập n="))
print("n=", n)
for i in range(1, n+1):

    for j in range(1, i+1):
        print(" * ", end="")

    print(end="\n\n")
# /=end ====================================================
"""
input n=5
output:
n=5
	* * * * *
	* * * *
	* * *
	* *
	*
/=end
"""
# Hướng dẫn:
"""
- Vòng for (i) ngoài lặp từ 1 -> n+1 => lặp theo hàng
	- Vòng for (j) bên trong lặp từ 1-> (n+1) - i => lặp in theo cột
Ex: n=5
i=1
	=> lặp n+1 - i vòng = 5 vòng
	j=1-5: * * * * *
i=2
	=> j lặp n+1-i = 5+1-2 = 4 vòng
	* * * *
...
i=5
	=> j lặp n+1-i = 5+1-5 = 1 vòng
	*
____________________________________________________________________
"""
print(end="\n")
print("n=", n)
for i in range(1, n+1):
    for j in range(1, n+1-i+1):
        print(" * ", end="")
    print(end="\n\n")
# /End for tam giác 2
# /=end ====================================================

# /Begin Tam giác 3
"""
n=5
* * * * *
  * * * *
    * * *
	  * *
	    *
"""
# Hướng dẫn:
for i in range(1, n+1):
    # In khoảng trắng trước
    for j in range(1, i):
        print("   ", end="")
    # In dấu *
    for j in range(1, n+2-i):
        print(" * ", end="")
    # xuống dòng tiếp hàng tiếp theo
    print(end="\n\n")

# /=end tam giác 3============================================

# /Begin Tam giác 4
"""
n=5
        *
	  * *
    * * *
  * * * *
* * * * *
"""
# Hướng dẫn
print("n=", n)
for i in range(1, n+1):
    # In khoảng trắng trước
    for j in range(1, n-i+1):
        print("   ", end="")
    # In ra dấu *
    for j in range(1, i+1):
        print(" * ", end="")
    # Xuống hàng
    print(end="\n\n")
# /=end tam giác 4============================================

# /= Begin tam giác * cân
"""
n=5
        * 
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *

"""
# Hướng dẫn:
"""
	dòng 1 (i=1) => 1(*)  ~ ( 2*i - 1) ~ 1
	dòng 2 (i=2) => 3(*)  ~ ( 2*i - 1) ~ 3 
	dòng 3 (i=3) => 5(*)  ~ ( 2*i - 1) ~ 5
"""
print("n=", n)
for i in range(1, n+1):
    # in ra khoảng trắng trước
    for j in range(1, n+1 - i):
        print("   ", end="")
    # In ra 2*i - 1 dấu *
    for j in range(1, 2*i):
        print(" * ", end="")
    # Xuống dòng để quay lại in dòng tiếp theo
    print(end="\n\n")
# /= end for
# /= End tam giác * can

# Bài tập
# Bài tập 1:
"""
input => n=5
output
n=5
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1

"""
# Bài tập:
"""
input => n=10
output
	n=10
	1
	2 3
	4 5 6
	7 8 9 10

input => n=14
output
	n=14
	1
	2  3
	4  5  6
	7  8  9  10
	11 12 13 14 
"""
# Bài tập 3:
# in bảng cửu chương

# Bài tập 4:
# in ra dãy số fibonaci:  <=n
# 1,1,2,3,5,8,13,...

# Bài tập 5:
# in ra dãy số amstrong có 3 chữ số
# Số amstrong: abc = a^3 + b^3 + c^3
# ví dụ: 153 = 1^3 + 3^3 + 5^3
