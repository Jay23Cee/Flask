from flask import Flask, jsonify



app = Flask(__name__)

books = [
    {
        'name': 'Green Eggs and Ham',
        'price': 7.99,
        'isbn': 9782371000193
    },
     {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 9782371000193
    }

 ]

print(__name__)

#Get Books
@app.route('/books')
def get_books():
    return jsonify({'books': books})

#Get /store
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value ={}
    for book in books:
        if book in books:
            return_value={
                'name': book["name"],
                'price' : book["price"]
            }
        return jsonify(return_value)

app.run(port=5000)