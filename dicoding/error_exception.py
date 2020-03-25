#===================================================
# PENANGANAN KESALAHAN (ERROR & EXCCEPTION HANDLING)
#===================================================

""" 
Ada dua jenis kesalahan berdasarkan kejadiannya:
1. Kesalahan sintaksis (syntax errors) atau sering disebut kesalahan penguraian (parsing errors)
2. Pengecualian (exceptions) atau sering disebut kesalahan saat beroperasi (runtime errors)
"""

# ===================
# KESALAHAN SINTAKSIS
# ===================

print('salah indentasi')
File "<stdin>",
 	print('salah indentasi')
 	^
IndentationError: unexpected indent

# Kesalahan Sintaks pada While
while True print('Hello World')
	File "<stdin>",
		while True print('Hello World')

# ===================
# PENGECUALIAN
# ===================	

print(angka)
Traceback (most recent call last):
	File "<stdin>", line 1, in <module>
NameError: name 'angka' is note defined

# Variable karena tidak sama
bukan_angka = '1'
bukan_angka + 2
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str