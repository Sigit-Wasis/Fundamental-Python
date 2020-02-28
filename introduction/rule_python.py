print("Aturan Penulisan Python")

# ===================
# Penulisan Statement
# ===================
# Statement merupakan sebuah instruksi atau kalimat perintah yang akan dieksekusi

print("Hello World");
print("Embun Code")
nama = "Sigit wasis subekti"

# Sedangkan jika ingin menuliskan satu baris maka dipisahkan dengan menggunakan tanda (;)
# Namun menurut style guide python tidak dianjurkan untuk menulis seperti ini

print("Ngoding lan Ngaji"); print("Fokuskan tujuanmu"); nama = "Sigit"; alamat = "Lampung"

# ================
# Penulisan String
# ================
# String merupakan teks atau kumpulan dari karakter. Dalam penulisannya bisa menggunakan petik 1, 2, dan 3.

judul = "Belajar Pemrograman Python"
penulis = 'Mr. Fulan'
rilis = """ februari """

# ================
# Penulisan Case
# ================
# Sifat python bersifat case-sensitive artinya IniBudi dengan inibudi itu beda.
## Snake Case digunakan pada:
## module_name, package_name, method_name, function_name, global_var_name dll
## Camel Case digunakan pada:
## ClassName, ExceptionName
## ALL CAPS digunakan pada:
## GLOBAL_CONSTANT_NAME

tema = "Melatih Logika"
Tema = "Melatih Logika"

# ======================
# Penulisan Blok Program
# ======================

username = input("apakah username anda? [Embun/Qodr]: ")

# Blok Percabangan If
if username == "Embun":
    print("Selamat Anda Berhasil")
    print("Atau Anda Gagal")

# Blok Percabangan For
i = 1
for i in range(10):
    print(i)
