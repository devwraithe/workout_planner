import os

from src.modules.database import exercise_database
from src.modules.user_fitness_data import get_user_fitness_data
from src.modules.workout_plan import generate_workout_plan, load_workout_plan


def check_existing_plan():
    # Check if a workout plan already exists
    if os.path.exists("workout_plan.json"):
        print("A workout plan already exists. Do you want to overwrite it? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            current_fitness, weekly_availability, user_goals = get_user_fitness_data()
            workout_plan = generate_workout_plan(current_fitness, weekly_availability, user_goals, exercise_database)
            return workout_plan
        else:
            return load_workout_plan()
