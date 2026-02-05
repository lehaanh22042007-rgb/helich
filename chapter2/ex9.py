#bài 9
n = input("mời nhập số nguyên dương 5 chữ số: ")
max_chu_so = n[0]
for i in n:
    if i > max_chu_so:
        max_chu_so = i
print("chữ số lớn nhất trong số đó là:", max_chu_so)
