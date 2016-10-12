import dryscrape
from bs4 import BeautifulSoup

session = dryscrape.Session()
my_url = "https://shop.harristeeter.com/store/BA7D6205#/"
session.visit(my_url)
response = session.body()
soup = BeautifulSoup(response, "lxml")

print "yoooooooo \n"

everything2 = soup.find_all('li', 'productList__product')
for part in everything2:
	name = part.find('div', 'first')
	name = name.find('div', 'productInfo')
	name = name.find('hgroup', 'productInfo__title')
	name = name.find('h3')
	price = part.find('div', 'second priceInfo')
	price = price.find('span', 'priceInfo__price')
	print name.string + " : " +  price.string

