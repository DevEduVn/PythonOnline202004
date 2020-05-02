# Dict lồng nhau
myDict = {
    1: "Devmaster",
    2: "Academy",
    3: {
        "A": "Welcome ",
        "B": "To ",
        "C": "Devmaster "
    }
}
print(myDict)
# Vòng lặp
for key in myDict.keys():
    print(key, ":=>", myDict[key])
