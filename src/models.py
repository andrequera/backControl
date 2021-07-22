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

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "empresa":self.empresa,
            "email": self.email,
            "telefono":self.telefono,
            # "cotizacion": list(map(lambda x: x.serialize(), self.cotizacion)),
            # "pedido": list(map(lambda x: x.serialize(), self.pedido))
    # do not serialize the password, its a security breach
            }


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

    def serialize(self):
        return {
            "id": self.id,
            "producto": self.producto,
            "descripcion":self.descripcion,
            "paletas": self.paletas,
            "botellas":self.botellas,
            "sku": self.sku,
            "total":self.total,
            "cliente_id": self.cliente_id,
            
    # do not serialize the password, its a security breach
            }


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

    def serialize(self):
        return {
            "id": self.id,
            "nombre_cliente": self.nombre_cliente,
            "fecha":self.fecha,
            "sku": self.sku,
            "producto":self.producto,
            "paleta": self.paleta,
            "cantidad":self.cantidad,
            "cliente_id": self.cliente_id,
            
    # do not serialize the password, its a security breach
            }


class Inventario(Base.Model):
    #__tablename__='inventario'
    id = Base.Column(Base.Integer, primary_key=True)
    skuinventario = Base.Column(Base.String(50))
    productoinventario = Base.Column(Base.String(50))
    paletainventario = Base.Column(Base.Integer)
    cantidadinventario = Base.Column(Base.Integer)
    precioinventario = Base.Column(Base.Integer)
    fechainventario = Base.Column(DateTime,default=datetime.datetime.utcnow())

    def serialize(self):
        return {
            "id": self.id,
            "skuinventario": self.skuinventario,
            "productoinventario":self.productoinventario,
            "paletainventario": self.paletainventario,
            "cantidadinventario":self.cantidadinventario,
            "precioinventario": self.precioinventario,
            "fechainventario":self.fechainventario,
           
            
    # do not serialize the password, its a security breach
            }


class Producto(Base.Model):
    #__tablename__='producto'
    id = Base.Column(Base.Integer, primary_key=True)
    nombre = Base.Column(Base.String(50))
    descripcion = Base.Column(Base.String(50))
    paleta = Base.Column(Base.Integer)
    cantidad = Base.Column(Base.Integer)
    sku = Base.Column(Base.String(50))
    inventario_id = Base.Column(Base.Integer, ForeignKey('inventario.id'))
    inventario = relationship(Inventario)

    def serialize(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion":self.descripcion,
            "paleta": self.paleta,
            "cantidad":self.cantidad,
            "sku": self.sku,
            "inventario_id": self.inventario_id,
                        
    # do not serialize the password, its a security breach
            }


class Pedidos_Productos(Base.Model):
    #__tablename__='pedidos_productos'
    id = Base.Column(Base.Integer, primary_key=True)
    pedido_id = Base.Column(Base.Integer, ForeignKey('pedido.id'))
    pedido = relationship(Pedido)
    producto_id = Base.Column(Base.Integer, ForeignKey('producto.id'))
    producto = relationship(Producto)

    def serialize(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "producto_id":self.producto_id,
           
    # do not serialize the password, its a security breach
            }





#    def to_dict(self):
#        return {}

## Draw from SQLAlchemy base
#render_er(Base, 'diagram.png')
