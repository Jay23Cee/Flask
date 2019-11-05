from flask import Flask, jsonify, request, Response
import json



app = Flask(__name__)


DEFAULT_PAGE_LIMIT = 3

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
    },
    {
        'name': 'A',
        'price': 7.99,
        'isbn': 9780394800165

    }



 ]

print(__name__)

#Get Books
@app.route('/books')
def get_books():
    return jsonify({'books': books})


#POST /BOOKS
#{ 
#
# }
def validBookObject(bookObject):
    if ( "name" in bookObject and "price" in bookObject and "isbn" in bookObject):
        return True
    else:
        return False

@app.route('/books', methods=['POST'])
def add_book( ):
    request_data = request.get_json()
    if(validBookObject(request_data)):
        new_book={
            "name":request_data['name'],
            "price": request_data['price'],
            "isbn" : request_data['isbn']

        }

        books.insert(0,request_data)
        response = Response("", 201, mimetype='application/json')

        response.headers['Location'] = "/books/"+ str(new_book['isbn'])
        return response
    else:
       invalidBookObjectErrorMsg = {
           "error": "Invalid book object passedinrequest",
           "helpString": "Data passed in similar to this {'name' :'bookname' , 'price':7.99, 'isbn': 1234567890}"
       }
       response = Response(json.dumps(invalidBookObjectErrorMsg),status =400, mimetype= 'applicaiton/json')
       return response
#Get /store
@app.route('/books/<int:isbn>')
def get_book_by_isbn(isbn):
    return_value ={}
    for book in books:
        if book["isbn"]==isbn:
            return_value={
                'name': book["name"],
                'price' : book["price"]
            }
            
    return jsonify(return_value)


#put /books/91283127312
#{
    #'name' : 'The Odyssey'
    #'price': 0.99
#}
@app.route('/books/<int:isbn>', methods =['PUT'])
def replace_book(isbn):
    request_data = request.get_json()
    new_book= {
        'name': request_data['name'],
        'price':request_data['price'],
        'isbn' : isbn
    }
    i = 0;
    for book in books:
        currentIsbn = book["isbn"]
        if currentIsbn == isbn:
            books[i] = new_book
        i +=1
    response = Response("", status=204)
    return response
    
app.run(port=5000)