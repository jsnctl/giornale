from controllers.translation_controller import TranslationController
import numpy as np
from entities.exercise import Exercise
from flask import current_app as app

controller = TranslationController()


def create_exercise(language, no_translations):
    exercise = Exercise()
    translations = controller.get_N_translations_by_language(language, no_translations)

    for translation in translations:
        exercise.add_translation(translation)

    return exercise


def create_random_exercise(no_translations):

    # TODO: this is total horseshit as its a call per translation
    #  should be refactored to a single DB call with a list of ids

    exercise = Exercise()

    random_seed = [np.random.randint(1, 100) for _ in np.arange(no_translations)]
    app.logger.info("Exercise from {0} Translations: ids {1}".format(no_translations, random_seed))

    for translation_id in random_seed:
        translation = controller.get_translation_by_id(translation_id)
        exercise.add_translation(translation)

    return exercise
