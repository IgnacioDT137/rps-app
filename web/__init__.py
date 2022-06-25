from flask import Flask

def createApp():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'runner'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/auth/')

    return app