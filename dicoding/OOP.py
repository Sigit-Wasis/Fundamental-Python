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

# =================================
# MEKANISME PEWARISAN (INHERITANCE)
# =================================

# Frasa kelas dasar adalah terjemahan dari bahasa inggris dari frasa base class.
# Frasa kelas turunan adalah terjemahan dari bahasa inggris dari frasa derived class.
# Frasa menimpa metode adalah terjemahan bahasa inggris dari frasa method override.

class Kalkulator(object):
	"""docstring for Kalkulator"""
	def __init__(self, nilai=0):
		self.nilai = nilai

	def tambah_angka(self, angka1, angka2):
		self.nilai = angka1 + angka2
		if self.nilai > 9: 
			print('Melebihi batas angka: {}'.format(self.nilai))
		return self.nilai	

# Mewarisi kelas KalkulatorKali dari Kalkulator
class KalkulatorKali(Kalkulator):

	def kali_angka(self, angka1, angka2):
		self.nilai = angka1 * angka2
		return self.nilai

	# Menimpa (Override) Metode dengan Nama yang Sama Dengan Kelas Dasar
	# Maka method tambah_angka diatas diganti dengan dibawah ini
	def tambah_angka(self, angka1, angka2)
		self.nilai = angka1 + angka2
		return self.nilai

# Pemanggilan class KalkulatorKali
kk = KalkulatorKali()
a  = kk.kali_angka(2, 3)
print(a)

b  = kk.tambah_angka(5, 6)
print(b)

# ========================================================================
# Pemanggilan Metode Kelas Dasar dari Kelas Turunan dengan Sintaksis Super
# ========================================================================
class KalkulatorTambah(Kalkulator):
	""" contoh mewarisi kelas kalkulator sederhana """

	def tambah_angka(self, angka1, angka2)
		if angka1 + angka2 <= 9: # fitur ini sudah oke di kelas dasar, gunakan yang ada saja
			super().tambah_angka(angka1, angka2) # panggil fungsi dari Kalkulator lalu isi nilai
		else: # ini adalah fitur baru yang ingin diperbaiki dari keterbatasan kelas dasar
			self.nilai = angka1 + angka2
		return self.nilai

# Fungsi Super() of pythonindo.com
# fungsi super mengembalikan attribute dan metode dari super objek (induk) suatu kelas.
class Mamalia(object):
	def __init__(self, mammalName):
		print(mammalName, 'adalah hewan berdarah panas.')

class kucing(Mamalia):
	"""docstring for kucing"""
	def __init__(self):
		print("Kucing punya empat kaki.")
		super().__init__('Kucing')

m1 = Kucing()		

# Jika Anda sebelumnya pernah belajar bahasa pemrograman yang memiliki variabel privat, 
# dimana variabel tersebut tidak dapat diakses kecuali dari objek yang bersangkutan, di Python hal tersebut tidak ada.

# ===================================
# PERNAK PERNIK TERKAIT STRUKTUR DATA
# ===================================
class pegawai:
	pass # definis kelas kosong

don = Pegawai() # membuat pegawai baru menjadi objek bernama don

# tambahkan item data data pada objek sebagai record
don.nama = 'Sigit'
don.bagian = 'Lampung'
don.gaji = 20000000
