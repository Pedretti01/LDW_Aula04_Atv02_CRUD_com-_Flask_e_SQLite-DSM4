from flask import Flask, render_template
from controllers import routes
from models.database import db
import os


app = Flask(__name__, template_folder='views')
routes.init_app(app)

# Permite Ler o diretório de um determinado arquivo
dir = os.path.abspath(os.path.dirname(__file__))

# Passamos o diretório ao SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(dir, 'models/boardgames.sqlite3')


if __name__ == '__main__':
    db.init_app(app=app)
    # Verifica no início da aplicação se o BD já existe. Caso contrário, cria o BD.
    with app.test_request_context():
        db.create_all()
    app.run(host='localhost', port=4000, debug=True)