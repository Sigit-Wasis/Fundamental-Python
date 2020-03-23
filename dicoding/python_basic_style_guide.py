# STATEMENT GABUNGAN
""" Usahakan untuk tidak menggabungkan >1 statement pada baris yang sama """

# Contoh Disarankan:
if foo == 'bash':
    do_blah_string()
do_one()
do_two()
do_three()

# PENGGUNAAN TRAILING COMMAS
""" Koma dibagian akhir umumnya bersifat opsional, satu statement dimana ia bersifat wajib adalah saat kita membuat
 variabel menggunakan tipe tuple dengan satu elemen."""

# Disarankan:
FILES = ('setup.crg',)

FILE = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILE,
           error=True,
           )

# ANOTASI FUNGSI
""" Penggunaan anotasi fungsi sebaiknya, menggunakan aturan baku untuk titik dua(:) dan menggunakan spasi untuk 
 penggunaan -> ."""

# Yes
def munge(input: AnyStr): ...
def munge() -> AnyStr: ...

""" Tidak menggunaka sama dengan(=) untuk mengindikasi keyword argumen atau nilai dasar pada parameter fungsi """

# Yes
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

""" Ketika melakukan kombinasi argumen anotasi dan nilai dasar, disarankan untuk menggunakan spasi sebelum dan sesudah = """

# Yes
def munge(sep: AnyStr = none): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

# PENAMAAN
""" Penamaan pada pustaka (library) Python agak sulit dibuat konsisten, mengingat jumlah paketnya sudah banyak 
dan terdapat beberapa library eksternal yang sudah tidak lagi dikelola. Konsisten internal lebih diutamakan """

# Prinsip Overriding
""" Nama yang dilihat oleh user publik (misalnya API) sebaiknya merefleksikan penggunaan/fungsinya, 
tidak merefleksikan implementasinya. Misal nama fungsi  """
cariJalan()

# Penamaan Deskriptif
"""
b (satu karakter huruf kecil)
B (satu karakter huruf besar)
hurufkecil
huruf_kecil_dengan_pemisah_kata_garis_bawah
HURUFBESAR
HURUF_BESAR_DENGAN_PEMISAH_GARIS_BAWAH
HurufBesarDiAwalKata (atau CapWords, CamelCase). Pastikan semua singkatan/akronim dituliskan dengan huruf besar, 
contohnya HTTPServerError, bukan HttpServerError.
hurufCampuran (mirip dengan CapWords, hanya berbeda di karakter paling awal)
Huruf_Besar_Di_Awal_Kata_Dengan_Garis_Bawah
"""

# Yang perlu diperhatikan dalam penamaan
# hindari karakter l (huruf L kecil), O (huruf O besar) atau I (huruf I besar) karena akan sulita membedakan angka 1 dan 0.

# Nama Paket dan Nama Modul
""" Nama Modul sebaiknya pendek/singkat, menggunakan huruf kecil dan opsional garis bawah (_) untuk meningkatkan keterbacaan. 
Nama Paket menggunakan huruf kecil dan hindari garis bawah(_). """

# Nama Kelas
""" Gunakan CamelCase atau CapWords convention. Pastikan semua akronim (misal HTTP) ditulis keseluruhan dengan huruf besar. """

# Penulisan Tipe Variable
# umumnya menggunakan CamelCase atau CapWords, lebih pendek lebih baik:
T, AnyStr, Num

""" Jika terdapat covariant atau contravariant dari sebuah variabel, tambahkan di akhir variabel untuk mempermudah pembacaan."""

from typing import TypeVar
VT_co = TypeVar('VT_co', covariant=True)
KT_contra = TypeVar('KT_contra', contravariant=True)

# Nama Exception
""" Karena exception seharusnya bertipe kelas, Anda juga menerapkan konvensi penamaan kelas pada exception. 
Bedanya, tambahkan “Error” atau nama deskriptif lain pada nama exception Anda. """

# Nama Variabel Global
""" Nama Variabel Global mengikuti fungsi/modul yang bersifat publik. anda bisa menggunakan garis bawah untuk
 menghindari variabel tersebut di-import jika ia merupakan modul non-publik """

# Nama Fungsi, Parameter, dan Variabel
""" Nama fungsi, parameter, variabel sebaiknya menggunakan huruf kecil, dengan pemisahan menggunakan garis bawah 
 untuk meningkatkan keterbacaan """

# Konstanta
""" Konstanta umumnya didefinisikan pada bagian atas modul dengan huruf besar, misalnya MAX_OVERFLOW dan TOTAL. """