# PERULANGAN (FOR)

""" 
Perulangan pada python tidak terbatas melainkan lebih ke fungsi yang dapat melakukan perulangan pada setiap jenis variabel 
Variabel yang dimaksud bisa berupa list, string, ataupun range.	
"""

# Contoh perulangan string python
for letter in 'python': # First Example
	print("Current Letter: {}". format(letter))

# perulangan list python
fruits = ['banana', 'apples', 'mango']
for fruit in fruits:	# Second Example
	print("Current Letter: {}". format(fruit))

# perulangan berdasarkan index/range dengan fungsi len()
fruits = ['banana', 'apples', 'mango']
for index in range(len(fruits)):
	print("Current Letter: {}". format(fruits[index]))

# perulangan angka 1 - 10
for i in range(1, 10):
	print(i)

# Perulangan Dictionary
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
	print("%s %d" % (i, d[i]))

# PERULANGAN (WHILE)

""" 
while pada bahasa python digunakan untuk mengeksekusi statement selama kondisi yang diberikan terpenuhi(True).
Tips: Python tidak memiliki do..while statement
"""

count = 0
while (count < 5):
	print("The count is: {}".format(count))
	count = count + 1
else:
	print("good!")

# Eksekusi statement while mungkin bersifaut infinit/infinite loop saat kondisi tidak pernah bernilai false.
var = 1
while var == 1: # The constructs an infinite loop
	num = input('Enter a number: ')
	print('You entered: {}'.format(num))

while True:
	num = input("Enter a number: ")
	print('You entered: {}'.format(num))

# PERULANGAN BERTINGKAT
for i in range(0, 5):
    for j in range(0, 5 - i):
        print(i, end=' ')
    print()