#+=+======++++=
# FUNGSI PYTHON
#+=+======++++=

""" Fungsi adalah blok kode yang terorganisasi dengan baik sehingga dapat digunakan kembali (reusable).
	Beberapa syarat fungsi umum adalah modularisasi dan fungsionalitasnya.
	Fungsi yang memanggil dirinya sendiri disebut fungsi rekursif.
"""

# ====================
# MENDEFINISKAN FUNGSI
# ====================

def functionname(parameters):
	"function_docstring"
	function_suite
	return [expression]

# Fungsi berikut akan menerima sebuah string sebagai parameter dan mencetaknya.
def printme(str):
	print(str)
	return

# Fungsi diatas akan sama dengan seperti berikut
def printme(str):
	print(str)

# ================
# MEMANGGIL FUNGSI
# ================

def printme(str):
	print(str)
	return 
# panggil
printme('Pemanggil Pertama')
printme('Pemanggil Kedua')

# ======
# RETURN
# ======
""" 
Pernyataan return [expression] akan membuat eksekusi program 
keluar dari fungsi saat itu, sekaligus mengembalikan nilai tertentu.
"""

# Example return
def sum(arg1, arg2):
	# Add both the parameters and return them.
	total = arg1 + arg2
	print('Inside the function: {}'.format(total))
	return total
# panggil sum
total = sum(20, 20)
print('Outside the function: {}'.format(total))

# Nilai kembalian dari sebuah fungsi dapat disimpan didalam sebuah variabel.

def kuadrat(x):
	return x*x
a = 10
k = kuadrat(a)
print('Nilai kuadrat dari {} adalah {}'.format(a, k))

# ==========================
# Pass by reference vs value
# ==========================
""" 
Seluruh parameter (argumen) pada bahasa Python bersifat “passed by reference”. 
Artinya saat Anda mengubah sebuah variabel, maka data yang mereferensi padanya 
juga akan berubah, baik di dalam fungsi, maupun di luar fungsi pemanggil. 
"""
def changeme(mylist):
	# append (menambah item di belakang)
	mylist.append([1, 2, 3, 4])
	print('Nilai di dalam fungsi: {}'.format(mylist))

# panggil changeme
mylist = [10, 20,30]
changeme(mylist)
print('Nilai di dalam fungsi: {}'.format(mylist))

# Contoh lain dimana argumen ditimpa dalam fungsi:
# Function definition is here
def changeme(mylist):
	"Variabel mylist berikut hanya dikenali (berlaku) di dalam fungsi"
	mylist = [1, 2, 3, 4]	# This would assign new reference in mylist
	print('Nilai di dalam fungsi: {}'.format(mylist))

# ARGUMEN FUNGSI
# BEBERAPA ARGUMENT YANG UMUM DIGUNAKAN:
"""
Required arguments : Argumen yang wajib disertakan dan disusun secara terurut dalam pemanggilan fungsi.
Keyword arguments : Argumen yang ditambahkan dengan menyertakan nama variabel/keywordnya dalam pemanggilan fungsi.
Default arguments : Argumen yang bersifat tidak wajib diisi, karena telah memiliki nilai default.
Variable-length arguments : Argumen yang bersifat opsional namun dapat disesuaikan banyaknya 
dan tidak didefinisikan secara spesifik dalam definisi fungsi.
"""

# Example Required Argument
def printme( str ):
	"This print a passed string into this function"
print str
# Now you can call printme function
printme()

# Example Keyword Argument
def printinfo(name, age):
	"This prints a passed info into this function"
	print('Name: ', name)
	print('Age: ',age)
# Now you can call printinfo function (with age argument first)
printinfo(name="sigit", age=19)

# Example Fungsi dengan Default Argument
def printinfo(name, age=35):
	"This prints a passed info into this function"
	print('Name: ', name)
	print('Age: ', age)
# Now you can call printinfo function (with optional argument age)
printinfo(age=5, name="Dicoding")
printinfo(name="Sigit")

# Fungsi berikut ini akan error saat didefiniskan 
# Argumen dengan nilai bawaan harus setelah argumen  tanpa bawaan
def printinfo(name="Data", Age):
	"This prints a passed info into this function"
	print('Name: ', name)
	print('Age: ', age)

# Contoh Implementasi Variable-length arguments
# Argumen posisi dapat bersifat dinamis dengan menambahkan sintaksis tanda bintang (*), untuk menampung kontainer (Tuple).
# Argumen kata kunci (keyword) dapat bersifat dinamis dengan menambahkan sintaksis dua tanda bintang (**) untuk menampung kontainer (Dictionary).
def printinfo(fixedarg, *args):
	"This prints a variabel passed arguments"
	print('Output: fixedarg {}'.format(fixedarg))
	for a in args:
		print('Argumen posisi {}'.format(a))

# Panggil printinfo
printinfo(10)
printinfo(70, 60, 50)

# Jika ada argumen posisi dinamis dan argument kata kunci (keyword) dinamis, maka urutannya adalah argumen posisi dahulu, baru argumen kata kunci.
def printinfo(*args, **kwargs):
	for a in args:
		print('Argumen posisi {}'.format(a))
	for key, value in kwargs.items():
		print('argument kata kunci {}:{}'.format(key, value))

# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **('i':7, 'j':8))


# FUNGSI ANONIM
""" Fungsi Anonim (anonymous) tidak dideklarasikan 
seperti halnya fungsi pada umumnya dengan kata kunci def, melainkan menggunakan kata kunci (keyword) lambda. 
"""
sum = lambda arg1, arg2: arg1 + arg2;
print('Value of total: ', sum(10, 20))
print('Value of total: ', sum(100, 245))

# CAKUPAN VARIABEL
""" Cakupan variabel umumnya dibagi menjadi 2: Variabel Lokal dan Variabel Global"""

# Example Code
total = 0 # Ini variabel global
def sum(arg1, arg2):
	# tambahkan kedua parameter dan return
	total = arg1 + arg2
	print('Inside the function Local: {}'.format(total))
	return total
# panggil sum
sum(10, 20)
print('Outside the function Global: {}'.format(total))

# Untuk mengenali variabel Global, tambahkan kata kunci (keyword) global saat memanggil nama variabel.
total = 0 # This is global variabel
# Fungsi didefiniskan di bawah ini
def sum(arg1, arg2):
	global total
	total = arg1 + arg2 #variabel local total
	print('Inside the function local total: ', total)
	return total

sum(10, 20)
print('Outside the function (global) total: ', total)