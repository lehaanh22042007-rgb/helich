#bài 13
a = int(input("nhập số a: "))
b = int(input("nhập số b: "))
if b != 0:
    print("a chia b bằng",a / b)
else:
    print("math error")
if type(a and b) != int:
    print("dữ liệu không hợp lệ mời nhập lại:")
    a = int(input("nhập số a: "))
    b = int(input("nhập số b: "))
else:
    pass
