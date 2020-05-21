from db.models import Translation


class TranslationController:

    def get_translation_by_id(self, id):
        result = Translation.query.filter_by(id=id).first()
        return result

    def get_N_translations_by_language(self, language, N):
        results = Translation.query.filter_by(language=language).limit(N).all()
        return results
