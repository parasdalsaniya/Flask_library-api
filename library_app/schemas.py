from library_app import ma


class MemberSchema(ma.Schema):
    class Meta:
        fields = ('mid', 'name', 'email', 'debt', 'amount_paid')


class BookSchema(ma.Schema):
    class Meta:
        fields = ('bid', 'title', 'author', 'average_rating',
                  'language_code', 'num_pages', 'ratings_count',
                  'text_reviews_count', 'publication_date',
                  'publisher', 'isbn', 'isbn13', 'stock', 'price')


class TransactionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'mid', 'bid', 'start_date',
                  'end_date', 'deadline', 'status', 'amount')


# init schema
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

# init schema
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# init schema
transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)
