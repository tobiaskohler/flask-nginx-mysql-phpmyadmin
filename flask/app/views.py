from app import app, db
from models import Users

@app.route("/", methods=["GET", "POST"])
def index():
    return "***Hello from Flask <3"

@app.route("/users/<username>", methods=["GET", "POST"])
def add_user(username):
    password = "test"
    add_user = Users(username, password)
    db.session.add(add_user)
    db.session.commit()

    return username