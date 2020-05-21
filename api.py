from flask import Flask
from flask_cors import CORS
from endpoints import translation_endpoint, exercise_endpoint
from extensions import db, api
import yaml

CREDENTIALS = yaml.load(open("./credentials.yaml", "rb"),
                        Loader=yaml.FullLoader)






def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CREDENTIALS['database']['db_url']
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    api.add_resource(translation_endpoint.TranslationByIdEndpoint, '/translation/<id>')
    api.add_resource(translation_endpoint.TranslationByLanguageEndpoint, '/translation/lang/<language>')

    api.add_resource(exercise_endpoint.ExerciseEndpoint, '/exercise')

    api.init_app(app)
    db.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)

