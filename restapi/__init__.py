from flask import Flask
from flask_cors import CORS
from restapi.views import incident_views, user_views
from flask_jwt_extended import jwt_required, JWTManager

app = Flask(__name__, instance_relative_config=True)
CORS(app)
app.register_blueprint(user_views.BP)
app.register_blueprint(incident_views.bp)
jwt = JWTManager(app)
app.config['JWT_SECRET_KEY'] = 'this is the secret key'
