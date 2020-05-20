from usecases.exercise_usecases import create_exercise


class ExerciseController:

    def generate_exercise(self, language, no_translations):
        exercise = create_exercise(language, no_translations)
        # TODO: persist to database
        return exercise

