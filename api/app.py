import connexion
import sys
from flask import jsonify

app = connexion.App(__name__, specification_dir='openapi/')

print(sys.path)

app.add_api('api.yaml')


@app.route("/")
def hello_world():
    return jsonify({'message':'Hello world!'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

