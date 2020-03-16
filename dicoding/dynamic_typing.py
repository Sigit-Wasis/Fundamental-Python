""" Python dikenal sebagai salah satu bahasa yang menerapkan dynamic typing,
yakni bahasa pemrograman yang hanya mengetahui tipe variabel saat program berjalan dan dilakukan assignment.
Tentu saja, pada Python juga umumnya tidak ada deklarasi variabel, hanya berupa assignment statement.
Cara ini adalah salah satu bentuk simplifikasi alokasi memori dalam bahasa Python.
Anda dapat selalu memeriksa tipe variabel yang digunakan dengan fungsi type() dan
memastikan tipe variabel yang tepat dengan metode isinstance(). Anda akan mempelajari lebih jauh mengenai fungsi
pada modul Fungsi dan mengenai class pada modul Pemrograman Berorientasi Objek."""

# Ketika kita memberikan nilai 6 pada variabel x
x = 6
print(type(x))
# Kemudian berika string "hello" pada variabel x di baris selanjutnya
x = 'hello'
print(type(x))

# +++++++++++++++++++
# Dynamic Typing pada Python
# +++++++++++++++++++

if False:
    1 + "two"           # Akan error jika dijalankan karena typeError dari kondisi
else:
    1 + 2

# +++++++++++++++++++
# Duck Typing
# +++++++++++++++++++
""""Jika sesuatu berjalan seperti bebek dan bersuara seperti bebek, maka kemungkinan besar ia adalah bebek"""
"""" Duck typing adalah sebuah konsep, tipe atau kelas dari sebuah obyek tidak lebih penting daripada 
metode yang menjadi perilakunya. Duck typing ini tidak terkait langsung dengan dynamic typing atau static typing, 
ini hanya memberikan keleluasaan pada developer untuk tidak perlu mencemaskan tentang tipe atau kelas dari sebuah obyek, 
yang lebih penting adalah kemampuan melakukan operasinya. Sehingga untuk memeriksa dan mengetahui tipe sebuah obyek,
 Anda cukup memastikan metode/fungsi/behavior dari obyek tersebut. Misalnya fungsi len() untuk mengetahui panjang string, 
 yang tidak berlaku pada variabel numerik (misalnya integer). """

data = "sdfasdfsafasdfasdf"
print(len(data))


