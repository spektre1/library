from .factory import create_app
from db import db

app = create_app(db)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
