from src.modules.database import exercise_database
from src.modules.user_fitness_data import get_user_fitness_data
from src.modules.workout_plan import display_workout_plan, generate_workout_plan

# Main program
if __name__ == "__main__":
    current_fitness, weekly_availability, user_goals = get_user_fitness_data()
    workout_plan = generate_workout_plan(current_fitness, weekly_availability, user_goals, exercise_database)
    display_workout_plan(workout_plan)
