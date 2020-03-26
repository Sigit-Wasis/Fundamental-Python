# ==================================
# PENANGANAN PENGECULIAN PYTHON
# ==================================
""" Proses penanganan penngecualian menggunakan pernyataan try yang berpasangan dengan expert """

z = 0
1 / z

# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

try:
	x = 1 / z
	print(x)
except ZeroDivisionError:
	print('tidak bisa membagi angka dengan nilai 0')

# maka hasilnya 'tidak bisa membagi angka dengan nilai 0'

try:
	with open('contoh_tidak_ada.py') as file:
		print(file.read())
except (FileNotFoundError, ):
	print('file tidak ditemukan')

# Di aplikasi yang lebih kompleks, penanganan pengecualian dapat menggunakan pernyataan except lebih dari satu
d = {'ratarata': '10.0'}

try:
	print('rata-rata: {}'.format(d['rata_rata']))
except KeyError:
	print('kunci tidak ditemukan di dictionary')
except ValueError:
	print('nilai tidak sesuai')
# Jawabannya : 'kunci tidak ditemukan di dictionary'

try:
	print('rata-rata: {}'.format(d['ratarata']/3))
except KeyError:
	print('kunci tidak ditemukan di dictionary')
except (ValueError, TypeError):
	print('nilai atau tipe tidak sesuai')
# Jawabannya : 'nilai atau tipe tidak sesuai'

try:
	print('pembulatan rata-rata: {}'.format(int(d['ratarata'])))
except (ValueError, TypeError) as e:
	print('penangan kesalahan: {}'.format(e))
# Jawabannya : 'penangan kesalahan: invalid literal for int() with base 10: '10.0''

""" ================================================================================================================
Bentuk lengkap dari pernyataan try dapat dilihat pada bagian berikut, terdiri dari pernyataan except, else, finally.
================================================================================================================"""

try:
	pass #gantikan Pernyataan yang mungkin terjadi pengecualian
except
	pass #gantikan Pernyataan dioperasikan jika terjadi pengecualian
else:
	pass #gantikan Pernyataan dioperasikan jika Tidak terjadi pengecualian
finally:
	pass #gantikan Pernyataan dioperasikan setelah semua pernyataan diatas terjadi

# ==============================================+
# Menghasilkan Pengecualian
# ==============================================+
""" Dalam membuat aplikasi, ada kemungkinan anda butuh untuk menghasilkan pengecualian (raise exceptions)
	salah satunya caranya bisa dengan menggunakan pengecualian yang sudah ada, hanya ditambah detail
"""

d = {'ratarata': '10.0'}

if 'total' not in d:
	raise KeyError('harus memiliki total')