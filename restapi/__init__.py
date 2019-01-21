from flask import Flask
from restapi.views import redflag_views, user_views

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(redflag_views.BPrint)
app.register_blueprint(user_views.BP)
