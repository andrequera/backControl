from flask_sqlalchemy import SQLAlchemy
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
#from sqlalchemy import render_er

db = SQLAlchemy()
#Base = declarative_base()
Base = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)


    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password":self.password,
    # do not serialize the password, its a security breach
            }

class Cliente(Base.Model):
    #__tablename__ = 'cliente'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Base.Column(Base.Integer, primary_key=True)
    nombre = Base.Column(Base.String(250), nullable=False)
    empresa = Base.Column(Base.String(250), nullable=False)
    email = Base.Column(Base.String(250), nullable=False)
    telefono = Base.Column(Base.Integer)

class Cotizacion(Base.Model):
    #__tablename__ = 'cotizacion'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Base.Column(Base.Integer, primary_key=True)
    producto = Base.Column(Base.String(250))
    descripcion = Base.Column(Base.String(250))
    paletas = Base.Column(Base.Integer, nullable=False)
    botellas = Base.Column(Base.Integer)
    sku= Base.Column(Base.String(250), nullable=False)
    total = Base.Column(Base.Integer)
    cliente_id = Base.Column(Base.Integer, ForeignKey('cliente.id'))
    cliente = relationship(Cliente)

class Pedido(Base.Model):
    #@__tablename__ = 'pedido'
    id = Base.Column(Base.Integer, primary_key=True)
    nombre_cliente = Base.Column(Base.String(50))
    fecha = Base.Column(DateTime,default=datetime.datetime.utcnow())
    sku = Base.Column(Base.String(50))
    producto = Base.Column(Base.String(50))
    paleta = Base.Column(Base.Integer)
    cantidad = Base.Column(Base.Integer)
    cliente_id = Base.Column(Base.Integer, ForeignKey('cliente.id'))
    cliente = relationship(Cliente)

class Inventario(Base.Model):
    #__tablename__='inventario'
    id = Base.Column(Base.Integer, primary_key=True)
    sku = Base.Column(Base.String(50))
    producto = Base.Column(Base.String(50))
    caja = Base.Column(Base.Integer)
    cantidad = Base.Column(Base.Integer)
    precio = Base.Column(Base.Integer)
    fecha = Base.Column(DateTime,default=datetime.datetime.utcnow())

class Producto(Base.Model):
    #__tablename__='producto'
    id= Base.Column(Base.Integer, primary_key=True)
    nombre = Base.Column(Base.String(50))
    descripcion = Base.Column(Base.String(50))
    paleta = Base.Column(Base.Integer)
    cantidad = Base.Column(Base.Integer)
    sku = Base.Column(Base.String(50), ForeignKey ('inventario.sku'))
    inventario = relationship(Inventario)

class Pedidos_Productos(Base.Model):
    #__tablename__='pedidos_productos'
    id = Base.Column(Base.Integer, primary_key=True)
    pedido_id = Base.Column(Base.Integer, ForeignKey('pedido.id'))
    pedido = relationship(Pedido)
    producto_id = Base.Column(Base.Integer, ForeignKey('producto.id'))
    producto = relationship(Producto)





#    def to_dict(self):
#        return {}

## Draw from SQLAlchemy base
#render_er(Base, 'diagram.png')











