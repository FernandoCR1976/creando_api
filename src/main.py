"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User_Fav, Planet, People, Vehicles
#from models import Person

from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this "super secret" with something else!
jwt = JWTManager(app)



# Generating new tokens


@app.route("/token", methods=["POST"])
def create_token():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    # Query your database for username and password
    user = User.filter.query(username=username, password=password).first()
    if user is None:
        # the user was not found on the database
        return jsonify({"msg": "Bad username or password"}), 401
    
    # create a new token with the user id inside
    access_token = create_access_token(identity=user.id)
    return jsonify({ "token": access_token, "user_id": user.id })

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user_id = get_jwt_identity()
    user = User.filter.get(current_user_id)
    
    return jsonify({"id": user.id, "username": user.username }), 200

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)

@app.route('/userfav', methods=['GET'])
def list_user():
    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/people', methods=['GET'])
def list_people():
    people = People.query.all()
    response_body = {
        "msg": "Hello, this is your GET /people ",
        'data': people


    }

    return jsonify(response_body), 200

@app.route('/planet', methods=['GET'])
def list_planet():
    planet = Planet.query.all()
    response_body = {
        "msg": "Hello, this is your GET /planet ",
        'data': planet
    }

    return jsonify(response_body), 200

@app.route('/vehicles', methods=['GET'])
def list_vehicles():
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        'data' : vehicles
    }
    return jsonify(response_body), 200


@app.route('/addAll', methods=['POST'])
def list_addAll():
    body = request.get_json()
    people = body['people'] 
    planet = body['planet']
    vehicles = body['vehicles']

    for p in people:
        people1 = People(
            name = p["Character Name"],
            heigth =p["Character heigth"],
            mass = p["Character mass"],
            hair_color = p["Character hair color"],
            skin_color = p["Character skin color"],
            eye_color = p["Caracter eye color"],
            birth_year = p["Character birth year"],
            gender = p["Character Gender"]

        )
        db.session.add(people1)

    for pl in planet:
        planet1 = Planet (
            planet_name = pl["Planet Name"],
            rotation_period = pl["Rotation Period"],
            orbital_period= pl["orbital Period"],
            diameter = pl["Diameter"],
            climate = pl["Climate"],
            gravity= pl["Gravity"],
            terrain = pl["Terrain"],
            population = pl["Population"]

        )
        db.session.add(planet1)

    for v in vehicles:
        vehicles1 = Vehicles (
            vehicle_name = v["Vehicle name"],
            model = v["Model"],
            passengers = v["Passengers"],
            consumable = v["consumable"],
            starship_class = v["Starship class"],
            length = v["Length"],
            cargo_capacity = v["Cargo capacity"],
            hyperdrive_rating = v["Hyperdrive rating"]

        )
        db.session.add(vehicles1)




        db.session.commit()
    
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
