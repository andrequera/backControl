"""empty message

Revision ID: adf241e8bed4
Revises: 
Create Date: 2021-07-20 19:42:52.099120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'adf241e8bed4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=250), nullable=False),
    sa.Column('empresa', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('telefono', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventario',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('skuinventario', sa.String(length=50), nullable=False),
    sa.Column('productoinventario', sa.String(length=50), nullable=True),
    sa.Column('paletainventario', sa.Integer(), nullable=True),
    sa.Column('cantidadinventario', sa.Integer(), nullable=True),
    sa.Column('precioinventario', sa.Integer(), nullable=True),
    sa.Column('fechainventario', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('skuinventario')
    )
    op.create_table('cotizacion',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('producto', sa.String(length=250), nullable=True),
    sa.Column('descripcion', sa.String(length=250), nullable=True),
    sa.Column('paletas', sa.Integer(), nullable=False),
    sa.Column('botellas', sa.Integer(), nullable=True),
    sa.Column('sku', sa.String(length=250), nullable=False),
    sa.Column('total', sa.Integer(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_cliente', sa.String(length=50), nullable=True),
    sa.Column('fecha', sa.DateTime(), nullable=True),
    sa.Column('sku', sa.String(length=50), nullable=True),
    sa.Column('producto', sa.String(length=50), nullable=True),
    sa.Column('paleta', sa.Integer(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('cliente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cliente_id'], ['cliente.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=True),
    sa.Column('descripcion', sa.String(length=50), nullable=True),
    sa.Column('paleta', sa.Integer(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=True),
    sa.Column('sku', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['sku'], ['inventario.skuinventario'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pedidos__productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pedido_id', sa.Integer(), nullable=True),
    sa.Column('producto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pedido_id'], ['pedido.id'], ),
    sa.ForeignKeyConstraint(['producto_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pedidos__productos')
    op.drop_table('producto')
    op.drop_table('pedido')
    op.drop_table('cotizacion')
    op.drop_table('inventario')
    op.drop_table('cliente')
    # ### end Alembic commands ###
