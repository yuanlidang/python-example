from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from micro import app

#db = SQLAlchemy(app)
db = SQLAlchemy( )
#migrate = Migrate(app,db)