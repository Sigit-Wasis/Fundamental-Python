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