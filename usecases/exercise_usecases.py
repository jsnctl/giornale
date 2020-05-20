from controllers.translation_controller import TranslationController
import numpy as np
from entities.exercise import Exercise

controller = TranslationController()


def create_exercise(language, no_translations):

    exercise = Exercise()
    translations = controller.get_N_translations_by_language(language, no_translations)

    for translation in translations:
        exercise.add_translation(translation)

    return exercise
