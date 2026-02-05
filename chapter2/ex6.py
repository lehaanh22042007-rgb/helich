#bài 6
def giai_thua(n):
    if n == 1:
        return 1
    return n * giai_thua(n - 1)
n = int(input("nhập số của bạn: "))
print(giai_thua(n))
