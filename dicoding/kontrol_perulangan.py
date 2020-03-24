# ===========
# BREAK
# ===========
""" Pernyataan break mengehentikan kemudian keluar, dilanjurkan dengan mengekesekusi pernyataan setelah blog perulangan """

# Contoh 1
for letter in 'Python': #First Example
	if letter == 'h':
		break
	print('Current letter: {}'. format(letter))

# Contoh 2
var = 10
while var > 0:
	print('Current variabel value: {}'. format(var))
	var = var - 1
	if var == 5:
		break

# ===========
# CONTUNUE
# ===========
""" Pernyataan continue akan membuat iterasi saat ini berhenti, kemudian iterasi selanjutnya, dan mengabaikan pernyataan yang ada di continue """

# Contoh 1
for letter in 'Python': 
	if letter == 'h': # maka huruf h akan hilang atau dilewati
		continue
	print('Current letter: {}'. format(letter))

# Contoh 2
for a in [0, 1, -1, 2, -2, 3, -3]: 
	if a <= 0:
		continue
	print('Elemen positif: {}'. format(a))

# Contoh 3
var = 10
while var > 0:
	var = var - 1
	if var == 5:
		continue
	print('Current variabel value: {}'. format(var))

# ==================
# ELSE SETELAH FOR
# ==================
""" Didalam python dikenal fungsi else setelah for, fungsinya pada perulangan yang bersifat pencarian. """

# for item in container:
# 	if search_something(item):
# 		# Found it!
# 		process(item)
# 		break
# else: 
# 	# Didn't find anyting!
# 	not_found_in_container()

# Lebih singkatnya
# if any(something_about(thing) for that_thing in container):
# 	do_something(that_thing)
# else:
# 	no_such_thing()

# Penggunaan for-else untuk pencarian bilangan prima maka dapat di tambah else
for n in range(2, 10):
	for x in range (2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n/x)
			break
	else:
		print(n, 'is a prime number')


# ==================
# ELSE SETELAH WHILE
# ==================
""" Pada statement while, blok statement else akan selalu dieksekusi saat kondisi while salah """
n = 5
while n > 0:
	n = n - 1
	if n == 2:
		break
	print(n)
else:
	print("Loop is finished")

# ==================
# PASS
# ==================
""" Digunakan jika menginginkan sebuah pernyataan atau blok pernyataan, namun tidak melakukan apapun
dan melanjutkan eksekusi sesuai dengan seharusnya, sifatnya null. """

for letter in 'Python':
	if letter == 'h':
		pass
		print('This is pass block')
	print('Current letter: {}'. format(letter))

# pass pada perulangan menggunakan isupper (Karakter dalam Huruf Besar)
for letter in 'pyThOn':
	if letter.isupper():
		pass # will process later
	else:
		print('Lower letter: {}', format(letter))

# Mengantisipasi kegagalan fungsi, contoh kode yang belum ada pass 
# maka jika diisi dengan huruf akan keluar dari inputan
# var1 = ""
# while(var1 != "Exit"):
# 	var1 = input("Please enter an integer (type exit to exit): ")
# 	print(int(var1))

# Kegagalan ketika menggunakan pass
# import sys
# data = ''
# while (data != 'exit'):
# 	try:
# 		data = input('Please enter an integer (type exit to exit): ')
# 		print('got integer: {}'.format(int(data)))
# 	except:
# 		if data == exit:
# 			pass 
# 		else:
# 			print('error: {}', format(sys.exc_info()[0]))

# LIST COMPREHESION (Membuat list dengan inline loop dan if)
""" List comprehension adalah cara mudah untuk mendefinisikan dan membuat list di Python. """

# Cara1
numbers = [1, 2, 3, 4]
squares = []
for n in numbers:
	squares.append(n**2)
print(squares)

# Cara2
number = [1, 2, 3, 4]
squares = [n**2 for n in numbers]
print(squares)

# Menemukan bilangan yang ada di kedua list
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = []
for a in list_a:
	for b in list_b:
		if a == b:
			# append(menambah nilai baru)
			common_num.append(a)
print(common_num)
print(20*'*')

# Contoh Implementasi dengan list comprehension
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]
common_num = [a for a in list_a for b in list_b if a == b]
print(common_num)

# Contoh kecilkan semua huruf
# lower (untuk mengecilkan semua huruf)
# dan underscore merupakan nama variable yang valid
list_a = ['Sigit', 'Wasis', 'Subekti']
small_list_a = [_.lower() for _ in list_a]
print(small_list_a)

# Kuis List Comprehension
""" 
1 (bilangan awal)
10 (bilangan akhir)
2 (kenaikan / jarak antara 1 - 10)
"""
list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)