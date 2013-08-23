from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {"DB": "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)


def register_blueprints(app):
    # Prevents circular imports
    from tumblelog.views import posts
    from tumblelog.admin import admin
    app.register_blueprint(posts)
    app.register_blueprint(admin)

register_blueprints(app)

if __name__ == '__main__':
    app.run()
