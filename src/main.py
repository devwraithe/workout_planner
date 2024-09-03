from src.modules.check_plan import check_existing_plan
from src.modules.workout_plan import display_workout_plan

# Main program
if __name__ == "__main__":
    workout_plan = check_existing_plan()
    display_workout_plan(workout_plan)
