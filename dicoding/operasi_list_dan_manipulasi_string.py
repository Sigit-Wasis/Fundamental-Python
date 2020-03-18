# Operasi pada urutan (sequences: List, Set, String) len()
""" Salah satu fungsi yang paling bermanfaat untuk List atau String adalah len() yang akan menghitung
panjang atau banyaknya elemen dari List (untuk String menjadi menghitung jumlah karakternya). """

l = [1,2,3,4,5,6,7,8,9]
s = set(l)
x = "Hello World"

print(l)
print(len(l))

print(s)
print(len(s))

print(x)
print(len(x))

# Penggabungan dan Replikasi
""" pada list juga dimungkinkan adanya penggabungan (+) dan replikasi (*) """

data = [1,2,3] + ['A', 'B', 'C']
print(data)

datas = ['A', 'B', 'C'] * 3
print(datas)

# Range
""" Fungsi range() memberikan deret bilangan dengan pola tertentu. """
