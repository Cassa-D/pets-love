from app.views.interest_views import bp_interest
from app.views.photo_view import bp_photo
from flask import Flask
from flask_jwt_extended import JWTManager
from environs import Env
from app.models import db, ma, mg

from app.views.owner_views import bp_owner
from app.views.dog_views import bp_dogs

from app.views.home import bp_home
from app.views.breed_views import bp_breed
from app.views.authorization_view import bp_authorization
from app.views.message_view import bp_message
from app.views.conversation_view import bp_conversation
from app.views.like_views import bp_like

configs = {
    'development': 'DevelopmentConfig',
    'production': 'ProductionConfig'
}


def create_app(config='production'):

    env = Env()
    env.read_env()

    app = Flask(__name__)

    app.config.from_object(f'config.{configs[config]}')

    JWTManager(app)

    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    app.register_blueprint(bp_owner)
    app.register_blueprint(bp_dogs)

    app.register_blueprint(bp_home)
    app.register_blueprint(bp_breed)

    app.register_blueprint(bp_authorization)
    app.register_blueprint(bp_message)
    app.register_blueprint(bp_conversation)

    app.register_blueprint(bp_like)
    app.register_blueprint(bp_photo)
    app.register_blueprint(bp_interest)

    return app
