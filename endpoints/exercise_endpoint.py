from flask import jsonify
from flask_restful import Resource
from controllers.exercise_controller import ExerciseController

controller = ExerciseController()


class ExerciseEndpoint(Resource):

    def get(self):
        exercise = controller.generate_exercise("italian", 15)
        return jsonify(exercise.translations)