""" Module python adalah berkas teks berekstensi .py yang berisikan kode python. 
Module umum sudah disediakan oleh python dan diinstall menggunakan PIP
dan Dapat membuat dan menghasilkan modul Python anda sendiri """

# MENULIS MODUL

# define a function
def world():
	print('Hello, World!')
	print('Sigit Wasis Subekti!')
# Menambahkan Variabel
nama = "Dicoding"

# Menambahkan Kelas
class Reviewer:
	def __init__(self, nama, kelas):
		self.nama = nama
		self.kelas = kelas

	def review(self):
		print("Reviewer " + self.nama + " Bertanggung jawab di kelas " + self.kelas)