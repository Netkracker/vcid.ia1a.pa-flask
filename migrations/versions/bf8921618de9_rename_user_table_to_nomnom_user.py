from alembic import op
import sqlalchemy as sa

# Revision ID
revision = 'bf8921618de9'
down_revision = '249fe2446a16'  # Deine vorherige Migration
branch_labels = None
depends_on = None

def upgrade():
    # 1. Foreign Key in der recipe-Tabelle entfernen
    op.drop_constraint('recipe_user_id_fkey', 'recipe', type_='foreignkey')

    # 2. user-Tabelle in nomnom_user umbenennen
    op.rename_table('user', 'nomnom_user')

    # 3. Foreign Key mit neuem Tabellennamen wieder hinzufügen
    op.create_foreign_key(
        'recipe_user_id_fkey', 'recipe', 'nomnom_user', ['user_id'], ['id']
    )

def downgrade():
    # Rückgängig machen der Änderungen
    op.drop_constraint('recipe_user_id_fkey', 'recipe', type_='foreignkey')
    op.rename_table('nomnom_user', 'user')
    op.create_foreign_key(
        'recipe_user_id_fkey', 'recipe', 'user', ['user_id'], ['id']
    )
