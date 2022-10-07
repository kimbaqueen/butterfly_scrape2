import requests
from bs4 import BeautifulSoup
import re


r = requests.get("https://butterfly-conservation.org/uk-butterflies/a-to-z")
soup = BeautifulSoup(r.text)


links = soup.find_all("a")
hrefs = [link.attrs.get('href') for link in links]
butterfly_pages = hrefs[39:100]

urls = ["https://butterfly-conservation.org/" + page for page in butterfly_pages]




def get_butterfly(url):
	"""Request and parse a single butterfly profile page, return a dict of data."""


	r = requests.get(url)
	soup = BeautifulSoup(r.text)

	h1 = soup.find("h1")
	name = h1.text
	name = name.strip()      # strip off whitespace at end of name

	family = soup.find("li", text=re.compile(r'Family:*'))
	size = soup.find("li", text=re.compile(r'Size:*'))
	wing_span = soup.find("li", text=re.compile(r'Wing Span:*'))


	return {
			'name': name,
			'family': peel_data_from_element(family), 
	        'size': peel_data_from_element(size), 
	        'wing span': peel_data_from_element(wing_span),
	        'url': url,
	       }


def peel_data_from_element(element):
	just_text = element.text
	return just_text.split(': ')[1]




print(get_butterfly(urls[0]))






