import os
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

db = SQLAlchemy()

class Migration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)

def run_migrations(app):
    migration_folder = os.path.join(app.root_path, 'migrations')
    if not os.path.exists(migration_folder):
        logger.info("No migrations folder found. Skipping migrations.")
        return

    with app.app_context():
        # Create the Migration table if it doesn't exist
        db.create_all()

        migration_files = sorted(f for f in os.listdir(migration_folder) if f.endswith('.sql'))

        for migration_file in migration_files:
            migration_record = Migration.query.filter_by(name=migration_file).first()
            
            if migration_record is None:
                with open(os.path.join(migration_folder, migration_file), 'r') as file:
                    migration_sql = file.read()
                
                logger.info(f"Running migration: {migration_file}")
                db.session.execute(text(migration_sql))
                
                new_migration = Migration(name=migration_file)
                db.session.add(new_migration)
                db.session.commit()
                logger.info(f"Migration {migration_file} completed successfully.")
            else:
                logger.info(f"Migration {migration_file} already applied. Skipping.")

        logger.info("All migrations completed successfully.")