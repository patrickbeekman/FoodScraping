import dryscrape
import time
from bs4 import BeautifulSoup


def calculatePrice(product):
	price = 0.00;
	words = product.find('div', 'second priceInfo')
	words = product.find('span', 'saleInfo__description1 text')
	if (words is not None): #if there is a sale price
		splitWords = words.string.split(' ')
		if (words.string[1] == '$'): #if the price is just a new price
			checkingPrice = words.string[2:6]
			if (checkingPrice.endswith("/lb") is True):
				checkingPrice = checkingPrice.strip("/lb")
			price =  float(checkingPrice)
		else: #if the price is a fraction ex. 10 for $10 so $1 each
			integer = str(splitWords[0])[1:2].strip("'")
			multiPrice = str(splitWords[2]).strip("$").strip("'")
			if (multiPrice.endswith("/lb") is True):
				multiPrice = multiPrice.strip("/lb")
			price = (float(multiPrice) / int(integer))
			#have to account for strings where 10 for 10 but also for strings that are 2 for 6.00
	else:	#if there is NO sale price
		btwnPrice = product.find('div', 'second priceInfo')
		btwnPrice = btwnPrice.find('span', 'priceInfo__price')
		if (btwnPrice.string.endswith("/lb")):
			btwnPrice = btwnPrice.string.strip("/lb")
			price = float(btwnPrice.strip("$"))
		else: 
			price = float(btwnPrice.string.strip("$"))
	return price

def findAllProducts(search_term):
	if (search_term == ""):
		my_url = "https://shop.harristeeter.com/store/BA7D6205#/"
	else:
		my_url = "https://shop.harristeeter.com/store/BA7D6205#/search/" + search_term  + "/1?queries=sort%3DRelevance"
	session = dryscrape.Session()
	session.visit(my_url)
	soup = BeautifulSoup(session.body(), "lxml")

	everything2 = soup.find_all('li', 'productList__product')
	for part in everything2:
		name = part.find('div', 'first')
		name = name.find('div', 'productInfo')
		name = name.find('hgroup', 'productInfo__title')
		name = name.find('h3')
		price = calculatePrice(part)
		print name.string + " : $%.2f" % price
	time.sleep(2)


search_term = ""
findAllProducts(search_term)

print "moving on...."

search_term = "pretzels"
findAllProducts(search_term)

print "moving on...."

search_term = "bees"
findAllProducts(search_term)


#I couldn't get this working for some reason
#q = session.at_xpath('//*[@id="searchBar"]')
#q.set(search_term)
#print(soup.find("div", "searchBar"))
#q2 = session.at_xpath('//*[@title="Search"]')
#q2.click()

