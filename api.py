from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
import yaml
import pandas as pd

CREDENTIALS = yaml.load(open("./credentials.yaml", "rb"),
                        Loader=yaml.FullLoader)

app = Flask(__name__)
api = Api(app)

engine = create_engine(CREDENTIALS['database']['db_url'])


class HeadlineSimple(Resource):
    def get(self, **kwargs):
        data = pd.read_sql("""SELECT * FROM headline LIMIT 10""", engine)
        return data['original_text'].to_json()

api.add_resource(HeadlineSimple, '/headline')

if __name__ == '__main__':
    app.run(debug=True)

