from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
from datetime import timedelta

from app.models import db
from app.models.owner_model import Owner

bp_authorization = Blueprint('authorization', __name__, url_prefix = '/auth')


@bp_authorization.route('/signup', methods = ['POST'])
def signup():

    data = request.get_json()
    owner = Owner(
        name = data['name'],
        surname = data['surname'],
        document = data['document'],
        email = data['email'],
        address = data['name'],
        # password = sha256(data['password']) -- tá aqui só pra lembrar de criptografar; substituir
        password = data['password']
    )
    
    print(owner.name)

    try:
        db.session.add(owner)
        db.session.commit()
        # db.session.close()
        
        return {'msg': f'created: {owner}'}, HTTPStatus.CREATED

    except IntegrityError:
        return {'error': HTTPStatus.BAD_REQUEST}, HTTPStatus.BAD_REQUEST


@bp_authorization.route('/login', methods = ['POST'])
def login():

    email = request.json.get('email')
    password = request.json.get('password') # criptografar
    owner = Owner.query.filter_by(email = email).filter_by(password = password).first() or None
    if not owner:
        return {"error": "Dados incorretos, tente novamente."}, 404

    access_token = create_access_token(
        identity = owner.id,
        expires_delta = timedelta(days = 10)
    )

    return {
        "data": {
            "name": owner.name,
            "userId": owner.id,
            "Access token": f"Bearer {access_token}"
        }
    }