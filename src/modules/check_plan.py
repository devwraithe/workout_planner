import json
import os

from src.modules.database import exercise_database
from src.modules.user_fitness_data import get_user_fitness_data
from src.modules.workout_plan import generate_workout_plan


def create_new_plan():
    try:
        current_fitness, weekly_availability, user_goals = get_user_fitness_data()
        workout_plan = generate_workout_plan(current_fitness, weekly_availability, user_goals, exercise_database)
        return workout_plan
    except Exception as e:
        print("An error occurred while creating the workout plan: ", e)
        return None


def load_plan_from_file():
    try:
        with open("workout_plan.json", "r") as file:
            workout_plan = json.load(file)
            return workout_plan
    except FileNotFoundError:
        print("No saved workout plan found.")
        return None
    except Exception as e:
        print("An error occurred while loading the workout plan: ", {e})
        return None


def confirm_plan_overwrite():
    while True:
        print("Are you sure you want to overwrite the existing plan? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            return create_new_plan()
        elif choice == "no":
            return load_plan_from_file()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")


def check_existing_plan():
    if not os.path.exists("workout_plan.json"):
        create_new_plan()

    while True:
        print("A workout plan already exists. Do you want to overwrite it? (yes/no)")
        choice = input().lower()
        if choice == "yes":
            return confirm_plan_overwrite()
        elif choice == "no":
            return load_plan_from_file()
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

