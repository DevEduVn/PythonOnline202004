"""
	Dictionary: => Key:Value
	"Name":"Chung Trịnh"
"""
# khởi tạo
myDict = dict()
# Gán giá trị
myDict["Name"] = "Chung Trịnh"
myDict["Age"] = 40
myDict["Address"] = "25 Vũ Ngọc Phan"

# In
print(myDict)
myDict["Name"] = "Donal Trump"
myDict["Age"] = 80
myDict["Address"] = "25 Vũ Ngọc Phan - Mỹ"

print(myDict)

# Keys
print("Keys:", myDict.keys())

# values
print("Values:", myDict.values())

# clear
myDict.clear()
print(myDict)
