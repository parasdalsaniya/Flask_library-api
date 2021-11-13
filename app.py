from library_app import app, db
import library_app.views

# db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
