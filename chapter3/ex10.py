#bài 10
numbers = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))
k = 0
for num in numbers:
    if num % 2 == 0:
        print(num)
        k = num + k
print("tổng các số chẵn trong ds:",k)
