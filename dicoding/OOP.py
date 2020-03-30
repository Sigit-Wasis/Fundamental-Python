# PENGENALAN PEMROGRAMAN BERORIENTASI OBJEK DENGAN PYTHON

""" Kelas atau dalam bahasa Inggris disebut class, merupakan sebuah konsep yang menyediakan sarana
untuk menyatukan data dan fungsionalitas secara satu kesatuan.
Catatan:
1. Kata objek adalah terjemahan bahasa inggris dari kata object
2. Kata Metode adalah terhemahan bahasa inggris dari kata method
"""

# ==========================
# CLASS
# ==========================
# class adalah cetak biru atau prototipe dari objek dimana kita mendefiniskan atribut dari suatu objek.

class NamaKelas:
	pass # gantikan dengan pernyataan misal: attribute dan method

# Example
class Kalkulator:
	""" Contoh kelas kalkulator sederhana """
	i = 12345

	def f(self):
		return "Hello World"

Kalkulator.i = 1024 # maka nilai atribute i akan terganti dengan 1024

# ======================================
# Objek (object: an instance of a class)
# ======================================

"""Pembahasan berikutnya adalah instantiation dari sebuah class, 
menggunakan notasi fungsi yaitu dengan kurung buka-kurung tutup, akan menghasilkan sebuah objek"""

# Example
k = Kalkulator() # membuat instance dari kelas jadi objek.
k.f() # akan mencetak hello world ke layar

# ==========================
# CLASS CONSTRUCTOR
# ==========================

""" Metode constructor ini bernama __init__ atau double underscore init. dan metode ini otomatis dipanggil dahulu. """
class Kalkulator():
	"""docstring for Kalkulator"""
	def __init__(self, i=12345):
		self.i = i # i variabel constructor

	def f(self):
		return 'hello world'

k = Kalkulator(i=2001) # melakukan instansiasi sekaligus mengisi attribute 1
print(k.i) # mencetak attribute i dari objek k

# ==========================
# METODE (METHOD)
# ==========================
""" Ada 3 jenis metode: metode dari objek, metode dari class, metode secara static
 Secara umum method adalah sebuah fungsi khusu yang menjadi milik suatu objek yakni instantiation dari class 
 Argumen self pada python tidak ada arti khusus, self standar penamaan agar mudah dimengerti pemrogram lain
 Fungsi decorator adalah sebuah fungsi yang mengembalikan fungsi lain, 
 biasanya digunakan sebagai fungsi transformasi dengan "pembungkus" sintaksis @wrapper
 """
# class method adalah sebuah fungsi yang mengubah metode menjadi metode dari class.

class Kalkulator():
	def f(self):
		return 'Hello World'

	@classmethod
	def tambah_angka(cls, angka1, angka2):
		return '{} + {} = {}'.format(angka1, angka2, angka1 + angka2)

	Kalkulator.tambah_angka(1, 2)

	k = Kalkulator()
	k.tambah_angka(1, 2)

# Static method sebuah fungsi yang mengubah metode menjadi metode static.

class Karyawati():

	def f(self):
		return "Hello World"

	@staticmethod
	def kali_wati(angka1, angka2):
		return '{}  x {} = {}'.format(angka1, angka2, angka1 * angka2)

	a = Kalkulator.kali_wati(2, 3)
	print(a)

	k = Kalkulator()
	a = k.kali_angka(2, 3)
	print(a)

# Example @classmethod dan @staticmethod of Geeks for Geeks
from datetime import date

class Person:
	def __init__(self, name, age):	
		self.name = name
		self.age = age

	# metode kelas untuk membuat objek Person pada tahun kelahiran.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# metode statis untuk memeriksa apakah Seseorang sudah dewasa atau tidak.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('Sigit', 19)
person2 = Person.fromBirthYear('Sigit', 2001)

print person1.age
print person2.age

print Person.isAdult(19)