import requests
from bs4 import BeautifulSoup

class Product:
  def __init__(self, title, price, actual_price, imgtag):
    self.title = title
    self.price = price
    self.actual_price = actual_price
    self.imgtag = imgtag

def scrap(query):
  url = "https://www.snapdeal.com/search"
  params = {
      "keyword": query
  }
  r = requests.get(url, params=params)
  soup = BeautifulSoup(r.content)
  products = soup.findAll('div', attrs={"class": "product-tuple-listing"})
  results = []
  for product in products:
    title = product.find('p', attrs={"class": "product-title"}).text
    price = product.find('span', attrs={"class": "product-desc-price"}).text
    actual_price = product.find('span', attrs={"class": "product-price"}).text
    imgtag = product.find('img')
    if "src" in imgtag.attrs:
      p = Product(title, price, actual_price, imgtag.attrs["src"])
    elif "data-src" in imgtag.attrs:
      p = Product(title, price, actual_price, imgtag.attrs["data-src"])
    results.append(p)
  return results
