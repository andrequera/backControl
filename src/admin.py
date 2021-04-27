import os
from flask_admin import Admin
from models import db, User, Cliente, Cotizacion, Pedido, Inventario, Producto, Pedidos_Productos, Base
from flask_admin.contrib.sqla import ModelView

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    
    # Add your models here, for example this is how we add a the User model to the admin
    admin.add_view(ModelView(User, db.session))

    # You can duplicate that line to add mew models
    admin.add_view(ModelView(Cliente, Base.session))
    admin.add_view(ModelView(Cotizacion, Base.session))
    admin.add_view(ModelView(Pedido, Base.session))
    admin.add_view(ModelView(Inventario, Base.session))
    admin.add_view(ModelView(Producto, Base.session))
    admin.add_view(ModelView(Pedidos_Productos, Base.session))
  