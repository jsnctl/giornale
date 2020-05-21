from usecases.exercise_usecases import create_random_exercise


class ExerciseController:

    def generate_exercise(self, language, no_translations):
        exercise = create_random_exercise(no_translations)
        # TODO: persist to database
        return exercise

