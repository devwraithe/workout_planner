import random

from src.modules.exercises_generation import generate_exercises


def generate_workout_plan(current_fitness, weekly_availability, user_goals, exercise_database):
    workout_plan = []

    # Generate a list of exercises suitable for the user's fitness level and goals
    suitable_exercises = generate_exercises(current_fitness, user_goals, exercise_database)

    for _ in range(weekly_availability):
        daily_workout = []
        for exercise in suitable_exercises[:random.randint(3, 5)]:
            if 1 in user_goals:  # Build muscle
                sets = 3
                reps = 8
            elif 2 in user_goals:  # Lose weight
                sets = 3
                reps = 12
            else:  # Improve endurance
                sets = 4
                reps = 15

            daily_workout.append({
                "name": exercise["name"],
                "sets": sets,
                "reps": reps,
                "rest": 90 if exercise["difficulty"] > 3 else 60
            })

        workout_plan.append(daily_workout)
        suitable_exercises = suitable_exercises[1:] + [suitable_exercises[0]]

    return workout_plan


def display_workout_plan(workout_plan):
    print("\nYour Workout Plan Is Ready:")
    for day, exercises in enumerate(workout_plan, start=1):
        print(f"\nDay {day}:")
        for exercise in exercises:
            print(
                f"- {exercise['name']}: {exercise['sets']} sets, {exercise['reps']} reps, {exercise['rest']}s rest")
