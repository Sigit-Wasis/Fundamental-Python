#===============================
# Indentasi
#===============================
""" Gunakan 4 spasi pada setiap tingkatan indentasi """

Statement tingkat 1:
    Statement tingkat 2()
    Statement tingkat 2 yang kedua()

#===============================
# Baris Lanjutan
#===============================
""" Gunakan hanging indent untuk menulis kode """

# Opsi 1
# Rata kiri dengan kurung atau pemisah dengan argumen utama
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# Opsi 2
# Tambahkan indentasi ekstra - (level indentasi baru) untuk memisahkan parameter/argument
def long_function_name(
        var_one, var_two, var_three,
        var_four);
    print(var_one)

# Opsi 3
# Hanging indents dengan penambahan level indentasi saja
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)

#===============================
# Kondisional(if)
#===============================

# Contoh kondisi visual yang tidak diubah/tanpa indentasi
if (sebuah kondisi dan
    kondisi yang lain);
    lakukanSesuatu()

# Tambahkan Komentar
if (sebuah kondisi dan
    kondisi yang lain);
    #Mengingat Keduanya Benar, lakukan hal berikut
    lakukanSesuatu()

# Tambahkan ekstra indentasi pada baris lanjutan
if (sebuah kondisi dan
        kondisi yang lain);
    lakukanSesuatu()

#===============================
# Kurung/siku penutup
#===============================

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)

#====================================================
# Mengganti baris: sebelum dan sesudah operator binary
#====================================================
""" File Encoding selalu menggunakan UTF-8(python3) dan ASCII(python2) """

income = (gross_Wages
          + texable_interest
          + (dividents - qualified_dividends)
          - ira_deducation
          - student_loan_interest)

#===============================
# Import
#===============================

yes: import os
     import sys

# atau dapat menggunakan:
from subprocess import Popen, PIPE

#===========================================
# Whitespace pada Expressions dan Statements
#===========================================

# antara kurung, kurawal, kurung siku
Yes: spam(ham[1], {eggs: 2})
# setelah koma tanpa argumen
Yes: foo = (0, )
# sebelum koma, titik dua, atau titik koma
Yes: if x == 4, print x, y; x, y = y, x
# memberikan paramenter pada fungsi
Yes: dct['key'] = lst[index]

