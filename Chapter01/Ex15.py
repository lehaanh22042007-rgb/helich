#bài 15
def greet():
    name = input("mời nhập tên sinh viên: ")
    a = float(input("mời nhập điểm toán: "))
    b = float(input("mời nhập điểm lý: "))
    c = float(input("mời nhập điểm hoá: "))

    print("tên:", name)
    print("điểm trung bình:", (a + b + c) / 3)

greet()
greet()
greet()
