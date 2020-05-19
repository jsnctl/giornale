from flask import jsonify
from flask_restful import Resource
from db.models import Translation


class TranslationByIdEndpoint(Resource):

    def get(self, id):
        result = Translation.query.filter_by(id=id).first()
        return jsonify(result)


class TranslationByLanguageEndpoint(Resource):

    def get(self, language):
        result = (
            Translation.query
                .filter_by(language=language)
                .limit(50)
                .all()
        )
        return jsonify(result)
