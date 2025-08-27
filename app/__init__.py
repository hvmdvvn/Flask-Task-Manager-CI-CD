from flask import Flask
from flasgger import Swagger
from .database import init_db
from .routes.user_routes import user_bp
from .routes.task_routes import task_bp
from .routes.health_routes import health_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "supersecret"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"

    # 👇 Add this Swagger config
    app.config['SWAGGER'] = {
        "title": "Task Manager API",
        "uiversion": 3,
        "openapi": "3.0.2",
        "swagger_ui": True,
        "specs_route": "/docs/",
        "servers": [
            {"url": "https://verbose-orbit-6975wg67wvpj3r9x6-5000.app.github.dev"}  # 👈 your Codespace URL
        ]
    }

    init_db(app)

    app.register_blueprint(user_bp, url_prefix="/api/users")
    app.register_blueprint(task_bp, url_prefix="/api/tasks")
    app.register_blueprint(health_bp, url_prefix="/")

    Swagger(app)

    return app

