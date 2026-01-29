#bài 7
a = float(input("nhập số a: "))
b = float(input("nhập số b: "))
c = float(input("nhập số c: "))
if a > b:
    if a > c:
        print(a,"là số lớn nhất")
    else:
        print(c, "là số lớn nhất")
elif b > a:
    if b > c:
        print(b, "là số lớn nhất")
    else:
        print(c, "là số lớn nhất")
