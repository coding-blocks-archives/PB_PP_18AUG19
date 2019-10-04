from flask import Flask, render_template, request

import product_scrapper

app = Flask("Comparator")

FRUITS = [
  {
    "id": 1,
    "name": "Apple"
  },
  {
    "id": 2,
    "name": "Orange"
  },
  {
    "id": 3,
    "name": "Guava"
  },
  {
    "id": 4,
    "name": "Kiwi"
  },
  {
    "id": 5,
    "name": "Mango"
  }
]

@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/fruits')
def fruits():
  return render_template('fruits.html', fruits = FRUITS)

@app.route('/fruits/<int:id>')
def fruit_info(id):
  for fruit in Fruits:
    if fruit["id"] == id:
      return render_template('fruit.html', fruit = fruit)
  return "No fruit found with this id."

@app.route('/scrapper', methods=['GET', 'POST'])
def scrapper():
  products = []
  if request.method == "POST":
    query = request.form["query"]
    products = product_scrapper.scrap(query)
  return render_template('scrapper.html', products = products)


if __name__ == '__main__':
    app.run(port = 5959, debug = True)
