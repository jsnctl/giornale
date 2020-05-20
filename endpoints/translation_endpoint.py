from flask import jsonify
from flask_restful import Resource
from controllers.translation_controller import TranslationController

controller = TranslationController()


class TranslationByIdEndpoint(Resource):

    def get(self, id):
        translation = controller.get_translation_by_id(id)
        return jsonify(translation)


class TranslationByLanguageEndpoint(Resource):

    def get(self, language):
        translations = controller.get_N_translations_by_language(language, 50)
        return jsonify(translations)