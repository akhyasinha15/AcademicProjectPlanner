from flask import Flask
from config import Config
from data.db import db
from presentation.routes import main_routes
from presentation.auth_routes import auth_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(main_routes)
app.register_blueprint(auth_routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)