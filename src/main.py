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
from models import db, User, Cliente, Cotizacion, Pedido, Inventario, Producto, Pedidos_Productos, Base
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, Base)
#db.init_app(app)
Base.init_app(app)
CORS(app)
setup_admin(app)

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

    users = User.query.all()
    all_users = list(map(lambda x: x.serialize(), users))

    return jsonify(all_users), 200

@app.route('/cliente', methods=['GET'])
def cliente():

    clientes = Cliente.query.all()
    all_clientes = list(map(lambda x: x.serialize(), clientes))

    return jsonify(all_clientes), 200

@app.route('/cotizacion', methods=['GET'])
def cotizacion():

    cotizaciones = Cotizacion.query.all()
    all_cotizaciones = list(map(lambda x: x.serialize(), cotizaciones))

    return jsonify(all_cotizaciones), 200

@app.route('/pedido', methods=['GET'])
def pedido():

    pedidos = Pedido.query.all()
    all_pedidos = list(map(lambda x: x.serialize(), pedidos))

    return jsonify(all_pedidos), 200

@app.route('/inventario', methods=['GET'])
def inventario():

    inventarios = Inventario.query.all()
    all_inventarios = list(map(lambda x: x.serialize(), inventarios))

    return jsonify(all_inventarios), 200



@app.route('/inventario', methods=['POST'])
def agregar_inventario():

    # First we get the payload json
    body = request.get_json()
    print(body)

    if body is None:
        raise APIException("You need to specify the request body as a json object", status_code=400)
    if 'skuinventario' not in body:
        raise APIException('You need to specify the sku', status_code=400)
    if 'productoinventario' not in body:
        raise APIException('You need to specify the producto', status_code=400)
    if 'paletainventario' not in body:
        raise APIException('You need to specify the paleta', status_code=400)
    if 'cantidadinventario' not in body:
        raise APIException('You need to specify the cantidad', status_code=400)
    if 'precioinventario' not in body:
        raise APIException('You need to specify the precio', status_code=400)
    if 'fechainventario' not in body:
        raise APIException('You need to specify the fecha', status_code=400)


    # at this point, all data has been validated, we can proceed to inster into the bd
    inventario1 = Inventario(skuinventario=body['skuinventario'], productoinventario=body['productoinventario'], paletainventario=body['paletainventario'], cantidadinventario=body['cantidadinventario'], precioinventario=body['precioinventario'], fechainventario=body['fechainventario'])
    Base.session.add(inventario1)
    Base.session.commit()
    return "ok", 200






@app.route('/producto', methods=['GET'])
def producto():

    productos = Producto.query.all()
    all_productos = list(map(lambda x: x.serialize(), productos))

    return jsonify(all_productos), 200

@app.route('/pp', methods=['GET'])
def pp():

    pps = Pedidos_Productos.query.all()
    all_pps = list(map(lambda x: x.serialize(), pps))

    return jsonify(all_pps), 200

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
