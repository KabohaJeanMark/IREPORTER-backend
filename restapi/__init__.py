from flask import Flask
from restapi.views import redflag_views, user_views
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(redflag_views.BPrint)
app.register_blueprint(user_views.BP)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'this is the secret key'