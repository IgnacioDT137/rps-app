from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'runner'

    from .views import views
    from .auth import auth
    from .files import files

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/auth/')
    app.register_blueprint(files, url_prefix = '/files/')

    return app