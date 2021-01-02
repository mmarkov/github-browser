from app import create_app
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from seed import SeedCommand


load_dotenv()
app = create_app()
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('seed', SeedCommand)

if __name__ == '__main__':
    manager.run()
