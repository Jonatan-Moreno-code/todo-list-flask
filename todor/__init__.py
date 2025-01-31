from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    #Configuracion del proyecto
    app.config.from_mapping(
        DEBUG = False,
        SECRET_KEY = 'dev',
        SQLALCHEMY_DATABASE_URI = "sqlite:///todolist.db"
    )

    #Inicialozamos la base de datos
    db.init_app(app)

    #Registrar blueprint
    from . import todo, auth
    app.register_blueprint(todo.bp)
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    #Para migrar los modelos que se crearan a la base de datos
    with app.app_context():
        db.create_all()
    
    return app