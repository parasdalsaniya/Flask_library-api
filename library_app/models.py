from library_app import db
from datetime import date


class Members(db.Model):
    mid = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    debt = db.Column(db.Integer(), default=0)
    amount_paid = db.Column(db.Integer(), default=0)

    # transaction = db.relationship("Transactions", backref="books", lazy=True)

    # def __init__(self, *argv):
    #     super(Members, self).__init__(*argv)

    def __init__(self, name, email):
        self.name = name
        self.email = email


class Books(db.Model):
    bid = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(300))
    author = db.Column(db.String(300))
    stock = db.Column(db.Integer())

    average_rating = db.Column(db.Integer())
    language_code = db.Column(db.String(10))
    num_pages = db.Column(db.Integer())
    ratings_count = db.Column(db.Integer())
    text_reviews_count = db.Column(db.Integer())

    publication_date = db.Column(db.Date(), default=date.today())
    publisher = db.Column(db.String(100))
    isbn = db.Column(db.String(300))
    isbn13 = db.Column(db.String(300))
    price = db.Column(db.Integer(), default=100)

    # transaction = db.relationship("Transactions", backref="books", lazy=True)

    def __init__(self, title, author, average_rating, language_code, num_pages, ratings_count, text_reviews_count, publisher, isbn, isbn13, stock, price):
        self.title = title
        self.author = author

        self.average_rating = average_rating
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count

        self.publisher = publisher
        self.isbn = isbn
        self.isbn13 = isbn13
        self.stock = stock
        self.price = price


class Transactions(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    mid = db.Column(db.Integer(), db.ForeignKey(
        "members.mid", ondelete="SET NULL"))
    bid = db.Column(db.Integer(), db.ForeignKey(
        "books.bid", ondelete="SET NULL"))
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date())
    deadline = db.Column(db.Date(), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Integer(), default=0)

    def __init__(self, mid, bid, start_date, end_date, deadline, status, amount):
        self.mid = mid
        self.bid = bid
        self.start_date = start_date
        self.end_date = end_date
        self.deadline = deadline
        self.status = status
        self.amount = amount
