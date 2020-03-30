# =========================================================
# Example @classmethod dan @staticmethod of Geeks for Geeks
# =========================================================

from datetime import date

class Person:
	def __init__(self, name, age):	
		self.name = name
		self.age = age

	# metode kelas untuk membuat objek Person pada tahun kelahiran.
	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year - year)

	# metode statis untuk memeriksa apakah Seseorang sudah dewasa atau tidak.
	@staticmethod
	def isAdult(age):
		return age > 18

person1 = Person('Sigit', 19)
person2 = Person.fromBirthYear('Sigit', 2001)

print person1.age
print person2.age

print Person.isAdult(19)