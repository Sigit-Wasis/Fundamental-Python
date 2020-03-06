import bs4
import requests
import csv

url = requests.get('https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptop')
soup = bs4.BeautifulSoup(url.text, 'html.parser')

containers = soup.select('.item-container')

# W(Write)
csv_file = open('Laptops.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Brand", "Produk", "Price"])

for container in containers:
	brands = container.select('.item-branding')
	brand = brands[0].img['title'].strip()

	products = container.select('.item-title')
	product = products[0].text.strip()

	prices = container.select('.price-current')
	price = prices[0].text.strip()

	print("Brand: " + brand)
	print("Product: " +	product)
	print("Price: " + price)