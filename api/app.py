import connexion
import sys
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

connexionApp = connexion.App(__name__, specification_dir='openapi/')
app = connexionApp.app

connexionApp.add_api('api.yaml')

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"

db = SQLAlchemy(app)

# NOTE: Must import Models before this!
with app.app_context():
    db.create_all()

@app.route("/")
def hello_world():
    return jsonify({'message':'Hello world!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

