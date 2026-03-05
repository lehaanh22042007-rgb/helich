#bài 3
mau = ["red", "green", "blue","orange","purple"]
try:
    mau.remove("green")
except ValueError:
    print("không có green trong danh sách")
print("danh sách sau khi xóa green",mau)
