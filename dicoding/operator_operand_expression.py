# OPERATOR DAN EKSPRESI (Expressions)
"""
Setiap logika komputasi yang berada dalam program anda akan menggunakan eksprsi. Sebuah ekspresi dapat terdiri dari
dari oprator dan operan. Salah satu conton termudah adalah a + b atau 2 + 3. maka + adalah operator dan a, b, 2, 3 sebagai
variabel/operand.
"""

a = 2 + 3
print(a)

b = 3 * 5
print(b)

# JENIS OPERATOR MATEMATIKA DAN STRING
""""
+ (tambah) => 3 + 5 = 8 dan 'a + b' = 'ab'
- (kurang) => 40 - 10 = 30 dan tidak berlaku untuk string
* (perkalian) => 2 * 5 = 10 dan 'la' * 3 menghasilkan 'lalala'
/ (pembagian) => 10 / 5 = 2 
** (pangkat) => 3 ** 4 = 81 dan untuk akar dua gunakan 0.5
// (pembagian habis dibagi /div) => 13 // 3 = 4 
% (modulus)
"""

perkalian = 'la' * 3
print(perkalian)

pangkat = 3 ** 4
akardua = 2 ** 0.5
print(pangkat)
print(akardua)

pembagians = 13 // 3
bagis = 15 // 2
print(pembagians)
print(bagis)

modulo = 15 % 2
print(modulo)

# OPERASI BIT
"""Bit adalah operator khusu untuk menangani operasi logika dalam bilangan biner dalam bentuk bit"""

x = 10
y = 12

# jika dicek hasilnya 0b1010
# Awalan 0b merupakan penanda bahwa ini adalah angka biner.
print('X berisi angka', x, 'desimal atau', bin(x), 'biner')
print('Y berisi angka', y, 'desimal atau', bin(y), 'biner')

# memberi jarak antar baris
print('\n')

# Operator And (&)
print('x & y :', x & y)
# Operator Or (|)
print('x | y :', x | y)
# Operator Xor (^)
print('x ^ y :', x ^ y)
# Operator Not (~)
print('~x :', ~x)
# Operator Left Shift (<<)
print('x << y :', x << y)
# Operator Right Shift (>>)
print('x >> y :', x >> y)

# PERBANDINGAN
""" Operator perbandinga digunakan untuk membandingkan 2 buah nilai """
A = 40
B = 60

print('A = ', A)
print('B = ', B)
print('\n')

# Operator sama dengan (==)
print('A == B :', A == B)
# Operator Tidak sama dengan (!=)
print('A != B :', A != B)
# Operator Lebih Besar (>)
print('A > B :', A > B)
# Operator Lebih Kecil (<)
print('A < B :', A  < B)
# Operator Lebih Besar Sama Dengan (>=)
print('A >= B :', A >= B)
# Operator Lebih Kecil Sama Dengan (<=)
print('A <= B :', A <= B)

# PENGGUNAAN le, lt, gt, ge, eq, ne
from operator import *
a = 1
b = 5.0
print('a =', a)
print('b =', b)
for func in (lt, le, eq, ne, ge, gt):
    print('%s(a, b):' % func.__name__, func(a, b))

# OPERATOR BOOLEAN
# not (boolean NOT)
# Jika C bernilai True, fungsi akan mengembalikan nilai False
C = True;
print(not C)

# and (boolean AND)
# X dan Y akan mengembalikan nilai False jika X bernilai false atau fungsi akan mengembalikan nilai Y.

X = True
Y = False
print(X and Y)

# or (boolean OR)
# X or Y, jika x bernilai True, fungsi akan mengembalikan nilai True atau fungsi akan mengembalikan nilai dari Y.
X = False
Y = True
print(X or Y)

# CARA SINGKAT MENULISKAN OPERASI
a = 2
a = a * 4
#  maka dapat ditulis
a = 2
a *= 4

# Urutan matematis dalam melakukan evaluasi
# misalkan 2 + 3 * 5 jika merujuka aturan yang benar maka dikalikan dahulu baru di tambah
# maka dipython dapat menggunakan tanda dalam kurung()
a = 2 + (3 * 5)
print(a)