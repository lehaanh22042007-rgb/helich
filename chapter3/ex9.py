#bài 9
numbers = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))
for num in numbers:
    if num % 2 == 1:
        print(num)
