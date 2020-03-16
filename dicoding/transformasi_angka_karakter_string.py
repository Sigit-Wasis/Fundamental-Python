# Transformasi angka
# Menambahkan awalan 0 pada angka
"""" Misalnya untuk nomor nota atau nomor antrian, Anda akan menemui kebutuhan menambahkan awalan 0
(0001 untuk angka 1, 0101 untuk angka 101, dan sebagainya). Anda dapat menggunakan fungsi zfill().
Catatannya adalah angka harus dikonversi ke string terlebih dahulu: """

x=1
print(type(x))
add = str(x).zfill(5)
print(add)

# Transformasi karakter dan string
# Metode upper() dan lower() dari String (dan karakter)
""" Method upper() dan lower() adalah metode konversi untuk membuat seluruh karakter dalam string 
menjadi kapital (upper) atau huruf kecil (lower). Jika terdapat karakter non huruf yang tidak 
memiliki opsi kapital, maka karakter tersebut tidak diubah. """

p = "Hello World!"
p = p.upper()
print(p)

p = p.lower()
print(p)

# isupper() dan islower()
""" Sementara isupper() dan islower() akan mengembalikan nilai boolean jika string yang dimaksud 
memiliki satu karakter dan seluruhnya kapital atau seluruhnya huruf kecil. Jika syarat tidak terpenuhi, 
maka fungsi/method akan mengembalikan nilai false. """

p = 'Hello World!'
u = "hello world"
x = "HELLO WORLD!"
print(p.islower())
print(u.islower())
print(x.isupper())

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('HELLO'.lower())
print('HELLO'.lower().islower())

# Metode isX dari String untuk Pengecekan
"""
isalpha() mengembalikan True jika string berisi hanya huruf dan tidak kosong.
isalnum() mengembalikan True jika string berisi hanya huruf atau angka, dan tidak kosong.
isdecimal() mengembalikan True jika string berisi hanya angka/numerik dan tidak kosong.
isspace() mengembalikan True jika string berisi hanya spasi, tab, newline, atau whitespaces lainnya dan tidak kosong.
istitle() mengembalikan True jika string berisi kata yang diawali huruf kapital dan dilanjutkan dengan huruf kecil seterusnya. 
"""
# Example
print('hello'.isalpha())
print('hello123'.isalpha())
print('hello'.isalnum())
print(' '.isspace())
print('123'.isdecimal())
print('This is Title Case'.istitle())
print('This Is Title Case'.istitle())

# Metode startswith() dan endswith() dari String
""" Fungsi startswith() dan endswith() akan mengembalikan nilai True berdasarkan nilai awalan atau akhiran string. 
Contohnya sebagai berikut: """

print('Hello World!'.startswith('Hello'))
print('Hello world!'.endswith('world!'))

# Metode join() dan split() dari String
""" Fungsi join() berguna saat Anda memiliki sejumlah string yang perlu digabungkan. Contohnya sebagai berikut: """

print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['my', 'name', 'is', 'Sigit']))
print('Qodr'.join(['adalah', 'komunitas', 'IT']))

""" Perhatikan bahwa string yang dioperasi dengan fungsi join() akan ditambahkan/disisipkan di antara 
setiap parameter/argument. Misalnya koma pada ‘cats, rats, bats’. Sebaliknya metode split() memisahkan 
substring berdasarkan delimiter tertentu (defaultnya adalah whitespace - spasi, tab, atau newline): """

print('my name is wasis'.split())
print('myABCnameABCisABCwasis'.split('ABC'))

# Teks rata kanan/kiri/tengah dengan rjust(), ljust(), dan center()
""" Anda dapat merapikan pencetakan teks di layar dengan rjust(), ljust() atau center(). rjust() dan ljust() 
akan menambahkan spasi pada string untuk membuatnya sesuai (misalnya rata kiri atau rata kanan). 
Argumennya berupa integer yang merupakan panjang teks secara keseluruhan (bukan jumlah spasi yang ditambahkan): """

print('Hello'.rjust(10))
print('hello'.rjust(20, '*'))
print('hello'.ljust(20, '-'))
print('keren'.center(20,'+'))

# Hapus Whitespace dengan strip(), rstrip(), dan lstrip()
""" Saat Anda menerima string sebagai parameter, seringkali masih terdapat karakter whitespace (spasi, tab, 
dan newline) di bagian awal dan atau akhir string yang dimaksud. Metode strip() akan menghapus whitespace 
pada bagian awal atau akhir string. lstrip() dan rstrip() akan menghapus sesuai dengan namanya, awal saja atau akhir saja: """

spam = '    hello   world   '
print(spam.strip())
print(spam.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS'))

# Mengganti string/substring dengan replace()
""" replace() adalah satu fungsi python yang mengembalikan string baru dalam kondisi 
substring telah tergantikan dengan parameter yang dimasukkan:"""

string = 'ngoding lan ngaji ngoding lan ngaji'
print(string.replace('ngoding', 'Ngoding'))
# parameter ketiga akan di ganti
print(string.replace('ngaji', 'Ngaji', 3))

