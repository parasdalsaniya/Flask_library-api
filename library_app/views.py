from library_app import app, db
from flask import request, jsonify
from .models import Books, Members, Transactions
from .schemas import *
from datetime import date


@app.route('/sum/<r>', methods=['GET'])
def sum(r):
    return r*r*r

# add member


@app.route('/member', methods=['POST'])
def add_member():
    name = request.json['name']
    email = request.json['email']
    new_member = Members(name, email)
    db.session.add(new_member)
    db.session.commit()
    return member_schema.jsonify(new_member)

# get all Members


@app.route('/member', methods=['GET'])
def get_members():
    all_members = Members.query.all()
    result = members_schema.dump(all_members)
    return jsonify(result)

# get one member


@app.route('/member/<mid>', methods=['GET'])
def get_member(mid):
    member = Members.query.get(mid)
    return member_schema.jsonify(member)

# update a member


@app.route('/member/<mid>', methods=['PUT'])
def update_member(mid):
    member = Members.query.get(mid)
    member.name = request.json['name']
    member.email = request.json['email']
    member.debt = request.json['debt']
    member.amount_paid = request.json['amount_paid']
    db.session.commit()
    return member_schema.jsonify(member)

# delete member


@app.route('/member/<mid>', methods=['DELETE'])
def delete_member(mid):
    member = Members.query.get(mid)
    db.session.delete(member)
    db.session.commit()
    data = member_schema.jsonify(member)
    data.headers.add('Access-Control-Allow-Origin', '*')
    return data


# add book
@app.route('/book', methods=['POST'])
def add_book():
    title = request.json['title']
    author = request.json['author']
    average_rating = request.json['average_rating']
    language_code = request.json['language_code']
    num_pages = request.json['num_pages']
    ratings_count = request.json['ratings_count']
    text_reviews_count = request.json['text_reviews_count']
    publisher = request.json['publisher']
    isbn = request.json['isbn']
    isbn13 = request.json['isbn13']
    stock = request.json['stock']
    price = request.json['price']

    new_demo = Books(title, author, average_rating, language_code, num_pages,
                     ratings_count, text_reviews_count, publisher, isbn, isbn13, stock, price)

    db.session.add(new_demo)
    db.session.commit()
    return book_schema.jsonify(new_demo)


# get all books


@app.route('/book', methods=['GET'])
def get_books():
    all_books = Books.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result)

# get one book


@app.route('/book/<bid>', methods=['GET'])
def get_book(bid):
    book = Books.query.get(bid)
    return book_schema.jsonify(book)

# update book


@app.route('/book/<bid>', methods=['PUT'])
def update_book(bid):
    book = Books.query.get(bid)
    book.title = request.json['title']
    book.author = request.json['author']
    book.average_rating = request.json['average_rating']
    book.language_code = request.json['language_code']
    book.num_pages = request.json['num_pages']
    book.ratings_count = request.json['ratings_count']
    book.text_reviews_count = request.json['text_reviews_count']
    book.publisher = request.json['publisher']
    book.isbn = request.json['isbn']
    book.isbn13 = request.json['isbn13']
    book.stock = request.json['stock']
    book.price = request.json['price']

    db.session.commit()
    return book_schema.jsonify(book)

# delete book


@app.route('/book/<bid>', methods=['DELETE'])
def delete_book(bid):
    book = Books.query.get(bid)
    db.session.delete(book)
    db.session.commit()
    data = book_schema.jsonify(book)
    data.headers.add('Access-Control-Allow-Origin', '*')
    return data


@app.route('/transaction', methods=['POST'])
def add_transaction():
    mid = request.json['mid']
    bid = request.json['bid']
    start_date = date.today()
    end_date = date.today()
    deadline = date.today()
    status = request.json['status']
    amount = request.json['amount']

    new_transaction = Transactions(mid, bid, start_date,
                                   end_date, deadline, status, amount)
    db.session.add(new_transaction)
    db.session.commit()
    return transaction_schema.jsonify(new_transaction)


# get all transactions


@app.route('/transaction', methods=['GET'])
def get_transactions():
    all_transactions = Transactions.query.all()
    result = transactions_schema.dump(all_transactions)
    return jsonify(result)
