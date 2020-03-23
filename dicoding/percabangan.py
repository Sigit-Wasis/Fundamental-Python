# PERCABANGAN
""" Beberapa contoh aplikasi dasar dalam percabangan:
 1. Genap dan Ganjil
 2. Positif dan Negatif
 3. Positif, Negatif dan Nol
 """

# IF
""" Tip: Python menganggap setiap nilai non-zero dan non-null sebagai True dan nilai zero/null sebagai False. """

var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)

# maka akan tidak tampil pada console untuk pengkondisian jika 0
var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)

# python nested IF statement
nilai1 = 75
nilai2 = 100

if nilai1 == 75:
    print("Nilai anda: ", nilai1)
    print("Step1")
    if nilai2 == 100:
        print('Nilai kamu: ', nilai2)
        print("Step2")

# Python Standar IF
nilai  = 50

if nilai == 70: # equal eksplisit
    print("nilai anda", nilai)

# fungsi is sinonim dari ==
if nilai is 90: # equal
    print("nilai anda", nilai)

if nilai is not 80: # not equal
    print("nilai anda bukan 80")

print("\n")
# memberi garis pada console
print(50*"=")

# Python if Elif
nilai = 74

if 80 <= nilai <= 100:
    print("Nilai Anda adalah A")
elif 70 <= nilai < 80:
    print("Nilai Anda adalah B")
elif 60 <= nilai < 70:
    print("Nilai Anda adalah C")
elif 50 <= nilai < 60:
    print("Nilai Anda adalah T, lakukan Perbaikan")
else:
    print("Maaf anda tidak lulus mata kuliah ini")

# Contoh lain Python IF-ELSE
amount = int(input("Enter amount: "))

if amount < 1000:
    discount = amount*0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount*0.10
    print("Discount", discount)
else:
    discount = amount*0.15
    print("Discount", discount)

print("Net payable: ", amount-discount)

print(10*'-=#')

# fungsi {} mengambil nilai pada variabel a dengan ('bilangan {}'. format(a))
a = 100

if a % 2 == 0:
    print('bilangan {} adalah positif'. format(a))
elif a < 0:
    print('bilangan {} adalah negatif'. format(a))
else:
    print('bilangan {} adalah nol'. format(a))

# TERNARY OPERATOR
""" Operator ternary juga dikenal sebagai ekspresi kondisional adalah operator yang mengevaluasi sesuatu berdasarkan 
kondisi apakah benar atau salah. Itu ditambahkan ke Python di versi 2.5. Ini hanya memungkinkan untuk menguji suatu 
kondisi dalam satu baris menggantikan multiline jika-jika membuat kode kompak. """

# Program to demonstrate conditional operator
a, b = 10, 20

# Copy value of a in min if a < b else copy b
min = a if a < b else b

print(min)

# ShortHand Ternary
""" Digunakan untuk membantu developer dalam memeriksa apakah ada error atau tidak """
output = None
msg = output or "dalam perbaikan"
print(msg)