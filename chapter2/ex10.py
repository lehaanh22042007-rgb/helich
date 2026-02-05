#bài 10
def tong(n):
    if n == 1:
        return 1
    return n + tong(n - 1)
n = int(input("nhập số của bạn: "))
print(tong(n))
