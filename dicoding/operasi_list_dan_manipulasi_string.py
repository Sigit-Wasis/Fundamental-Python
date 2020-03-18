# Operasi pada urutan (sequences: List, Set, String) len()
""" Salah satu fungsi yang paling bermanfaat untuk List atau String adalah len() yang akan menghitung
panjang atau banyaknya elemen dari List (untuk String menjadi menghitung jumlah karakternya). """
from typing import Tuple

l = [1,2,3,4,5,6,7,8,9]
s = set(l)
x = "Hello World"

print(l)
print(len(l))

print(s)
print(len(s))

print(x)
print(len(x))

# PENGGABUNGAN DAN REPLIKASI
""" pada list juga dimungkinkan adanya penggabungan (+) dan replikasi (*) """

data = [1,2,3] + ['A', 'B', 'C']
print(data)

datas = ['A', 'B', 'C'] * 3
print(datas)

# RANGE
""" Fungsi range() memberikan deret bilangan dengan pola tertentu. """
""" Fungsi range dapat memiliki 1-3 parameter """

# 1. range dengan 1 parameter n; membuat deret bilangan yang dimulai dari 0, sebanyak n bilangan.
for i in range(9):
    print(i)

# 2. range dengan 2 parametere n,p: membuat deret bilangan yang dimulai dari n, hingga sebelum p(bilangan p tidak ikut).
print('batas range')
for u in range(3, 9):
    print(u)

# 3. range dengan 3 parameter n,p,q; membuat deret bilangan yang dimulai dari n, hingga sebelum p dengan elemen selisihnya q.
print('batas range')
range3 = [_ for _ in range(1, 9, 2)]
print(range3)

# In dan not In
""" Untuk mengetahui sebuah nilai atau objek ada dalam list, Anda dapat menggunakan operator in dan not in. 
Fungsi ini akan mengembalikan nilai boolean True atau False."""

tes_in = 'hi' in ['hello', 'hi', 'howdy', 'heyas']
print(tes_in)

spam = ['hello', 'hi', 'howdy', 'heyas']
print('car' in spam)
print('howdy' not in spam)
print('cat' not in spam)

# Memberikan nilai (assignment) untuk lebih dari 1 variabel sekaligus
cat = ['fat', 'orange', 'loud']    # From list
col_cat = size, color, disposition = cat
print(col_cat)

# SORT
""" List dapat diurutkan dengan method sort() """
x = [2, 5, 3.14, 1, -7]
x.sort()
print(x)

buah = ['apel', 'rambutan', 'durian', 'alpukat', 'semangka']
buah.sort()
print(buah)
#  Urutan dapat memasukkan keyword reverse=True untuk menjadikan urutan yang sebaliknya.
buah.sort(reverse=True)
print(buah)

# Tiga hal yang perlu Anda ingat dalam metode sort:"""
""" 
1. Metode sort langsung melakukan pengurutan pada variabel yang dioperasikannya, sehingga tidak perlu
operasi assignment(=)
2. Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya.
maka akan terjadi error.
"""
# z = [1, 2, 3, 4, 'Alice', 'Bob']
# z.sort()
# print(z)

"""
3. Metode sort menggunakan urutan ASCII, sehingga nilai huruf kapital(uppercase) akan lebih dahulu dibandingkan huruf kecil. 
"""
m = ['Kucing', 'Kerbau', 'Ayam', 'Monyet', 'kambing', 'serigala', 'angsa']
m.sort()
print(m)

# Untuk mengatasi kendala ini, Anda dapat memasukkan keyword str.lower sebagai argumen metode sort.
# Hal ini akan membuat metode sort menganggap semua objek menggunakan huruf kecil, tanpa mengubah kondisi asli dari objek tersebut.

spam = ['a', 'A', 'z', 'Z']
spam.sort(key=str.lower)
print(spam)

# MANIPULASI STRING
# String atau teks adalah salah satu bentuk data yang akan Anda olah dalam program.

# STRING LITERALS
# umumnya string ditulis dengan mudah di python, diapit oleh tanda petik tunggal. Tapi kondisi dibutuhkan petik tunggal ditengah string
# Seperti : 'That is Alice's cat' maka python mengira bahwa petik alice's adalah penutup string.
# Namun dalam python dapat menggunakan Escape Character (Umumnya diawali dengan blackslash(\)
"""
Beberapa contoh Escape Character
\'         Single quote
\"         Double quote
\t         Tab
\n         Newline (line break)
\\         Backslash
"""
# Example
print("Hello three!\nHow are you?\nI\'m doing fine.")

"""
Selain tanda kutip dan kutip-dua, untuk penulisan string di python juga bisa menggunakan 3 tanda kutip.
"""
multi_line = """Hello three!
How are you
I'm fine.!"""
print(multi_line)

# RAW STRING
# Python juga menyediakan cara untuk memasukkan string sesuai dengan apapun input atau teks yang diberikan.
print(r'That is Carol\'s cat.')





