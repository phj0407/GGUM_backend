from flask import Blueprint, Flask
from provider.user import bp_user
from provider.diary import bp_diary
from provider.notice import bp_notice
from provider.survey import bp_survey
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
bind_api = Blueprint('api', __name__, url_prefix='/api')

app.register_blueprint(bp_user)
app.register_blueprint(bp_diary)
app.register_blueprint(bp_notice)
app.register_blueprint(bp_survey)

@app.route('/')
def main():
    return 'home_page'