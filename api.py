from flask import Flask
from controllers.translation_controller import \
    (TranslationByIdEndpoint, TranslationByLanguageEndpoint)
from extensions import db, api
import yaml

CREDENTIALS = yaml.load(open("./credentials.yaml", "rb"),
                        Loader=yaml.FullLoader)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = CREDENTIALS['database']['db_url']

    api.add_resource(TranslationByIdEndpoint, '/translation/<id>')
    api.add_resource(TranslationByLanguageEndpoint, '/translation/lang/<language>')

    api.init_app(app)
    db.init_app(app)

    return app


if __name__ == '__main__':
    create_app().run(debug=True)

