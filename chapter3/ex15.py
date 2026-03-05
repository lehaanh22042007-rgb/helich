#bài 15
#dùng slicing
s = input("Nhập chuỗi: ")
reverse_s = s[::-1]
print("Chuỗi sau khi đảo:", reverse_s)
#không dùng slicing
s = input("Nhập chuỗi: ")
reverse_s = ""
for char in s:
    reverse_s = char + reverse_s
print("Chuỗi sau khi đảo:", reverse_s)
