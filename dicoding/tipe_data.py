# Tipe Data

# Numbers
""" Tipe numerik di python dibagi 3: Int, Float, Complex """

a = 5
print(a, "is of type", type(a))
a = 2.5
print(a, "is of type", type(a))
a = 1+2j
print(a, "is complex number?", isinstance(1+2j, complex))

""" Integer tidak dibatasi oleh angka atau panjang tertentu, namun dibatasi oleh memori yang tersedia. 
Sehingga Anda tidak perlu menggunakan variabel yang menampung big number misalnya long long (C/C++), biginteger, atau sejenisnya. 
Contoh kode untuk menunjukkan bahwa Python tidak membatasi output integer adalah pencarian bilangan ke-10.000 pada deret fibonacci 
(catatan: bilangan ke-10.000 pada deret fibonacci memiliki panjang 2.090 digit) sebagai berikut:"""

x=[0]*10005;                                # inisialisasi array 0 sebanyak 10005; x[0]=0
x[1]=1                                      # x[1]=1

for j in range(2, 10001):
    x[j]=x[j-1]+x[j-2]                      # fibonanci
print(x[10000])

""" Perhatikan bagaimana Python melakukan pemotongan pada digit ke 16 pada variabel float b.Float atau bilangan pecahan 
dibatasi akurasinya pada 15 desimal. Yang membedakan Integer dan Float adalah titik (decimal points). 
Misalnya dalam penulisan angka 1 jenisnya Integer, tapi jika dituliskan sebagai 1.0 artinya berjenis Float atau pecahan."""

b = 8.1234567890123456
print(b)

""" Karena Python banyak digunakan juga oleh matematikawan, tipe bilangan di Python juga mendukung bilangan imajiner 
dan bilangan kompleks. Nilai bilangan kompleks (complex) dituliskan dalam formulasi x + yj, 
yakni bagian x adalah bilangan real, dan y adalah bilangan imajiner. Contohnya adalah sebagai berikut: """

a = 123456789123456789234123412412341234
print(a)

c = 1+2j
print(c)

# Strings
""" String adalah urutan dari karakter unicode. Dideklarasikan dengan petik tunggal dan ganda. """

s = "SIGIT WASIS SUBEKTI"
print(s[6])

# Boolean
""" Tipe data boolean merupakan turunan dari bilangan bulat (integer atau int) yang hanya 2 nilai: True / False """

# List
""" 
    x[0] artinya mengambil elemen paling awal, dengan index 0 dari List x
    x[5] artinya mengambil elemen dengan index 0 dari List x
    x[-1] artinya mengambil elemen dengan index paling belakang ke-1 dari List x
    x[3:5] artinya membuat list dari anggota elemen list x dengan index 3 hingga sebelum index 5 (tidak termasuk elemen
            dengan index 5, dalam hal ini hanya index 3-4
    x[:5] artinya membuat list dari anggota elemen list x paling awal hingga sebelum index 5 (tidak termasuk elemen 
            dengan index 5, dalam hal ini hanya index 0-4
    x[-3:] artinya membuat list dari anggota elemen list x mulai dari index ke-3 dari belakang hingga paling  belakang
    x[1:7:2] artinya membuat list dari anggota elemen list x dengan index 1 hingga sebelum index 5, dengan "step" 
            2(dalam hal ini hanya index 1,3,5)
"""

x = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(x[5])
print(x[-1])
print(x[3:5])
print(x[:5])
print(x[-3:])
print(x[1:9:2])

# Tuple
""" Tuple adalah jenis tipe data yang tidak dapat diubah elemenya. """

t = (5, "program", 2+7j)
print(t[1])
print(t[0:3])
# t[0]=10

# Set
""" Set merupakan kumpulan item bersifat unik dan tanpa urutan. 
Didefinisikan dengan kurawal dan elemennya dipisahkan dengan tanda koma. """

a = {1,2,3,4,5,6}
# a[1]

# Dictionary
""" Dictionary adalah kumpulan pasangan kunci-nilai (pair of key-value) yang sifanya tidak berurutan
    1. Setiap elemen pair key-value dipisahkan dengan koma(,)
    2. Key dan Value di pisahkan dengan titik dua(;)
    3. Key dan Value dapat berupa tipe variabel/objek apapun 
"""

d = {1:'value', 'key':3}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);