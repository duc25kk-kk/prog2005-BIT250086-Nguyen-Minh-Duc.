import math

def is_even(n):
    return n % 2 == 0

print("=== Bài 1: Kiểm tra số chẵn ===")
n = int(input("Nhập số nguyên: "))
print("Kết quả:", is_even(n))

print("\n=== Bài 2: Tìm số lớn nhất ===")
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
print("Số lớn nhất là:", max(a, b, c))

print("\n=== Bài 3: Hàm greet ===")

def greet(name="Student"):
    print(f"Hello, {name}!")

greet()
greet(input("Nhập tên của bạn: "))

print("\n=== Bài 4: Kiểm tra tuổi ===")
try:
    age = int(input("Nhập tuổi: "))
    if 1 <= age <= 120:
        print("Tuổi hợp lệ")
    else:
        print("Tuổi không hợp lệ")
except:
    print("Lỗi nhập dữ liệu")

print("\n=== Bài 5: Đếm ký tự 'a' ===")
text = input("Nhập chuỗi: ")
print("Số lượng 'a':", text.count('a'))

print("\n=== Bài 6: Đổi độ C sang độ F ===")
c = float(input("Nhập độ C: "))
f = c * 9 / 5 + 32
print(f"{c}°C = {f:.2f}°F")

print("\n=== Bài 7: Tính BMI ===")
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))
bmi = weight / (height * height)
print(f"BMI = {bmi:.2f}")

print("\n=== Bài 8: Phép chia ===")
try:
    x = int(input("Nhập số thứ nhất: "))
    y = int(input("Nhập số thứ hai: "))
    print("Kết quả:", x / y)
except ZeroDivisionError:
    print("Không thể chia cho 0")
except:
    print("Dữ liệu không hợp lệ")

print("\n=== Bài 9: Căn bậc hai ===")
num = float(input("Nhập số: "))
if num < 0:
    print("Lỗi: số âm")
else:
    print("Căn bậc hai:", math.sqrt(num))

print("\n=== Bài 10: Thông tin sinh viên ===")
for i in range(3):
    print(f"\nSinh viên {i + 1}:")
    name = input("Tên: ")
    toan = float(input("Toán: "))
    ly = float(input("Lý: "))
    hoa = float(input("Hóa: "))

    avg = (toan + ly + hoa) / 3
    print(f"{name} - Điểm trung bình: {avg:.2f}")