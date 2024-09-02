import random

# Exercise Database
exercise_database = [
    {
        "name": "Barbell Bench Press",
        "muscle_groups": ["chest", "shoulders", "triceps"],
        "equipment": ["barbell", "weights"],
        "difficulty": 3
    },
    {
        "name": "Bicep Curl",
        "muscle_groups": ["biceps"],
        "equipment": ["dumbbell"],
        "difficulty": 2
    },
    {
        "name": "Squat",
        "muscle_groups": ["quadriceps", "glutes", "hamstrings"],
        "equipment": ["barbell", "weights"],
        "difficulty": 4
    },
    {
        "name": "Push-ups",
        "muscle_groups": ["chest", "shoulders", "triceps"],
        "equipment": [],
        "difficulty": 2
    },
    {
        "name": "Pull-ups",
        "muscle_groups": ["back", "biceps"],
        "equipment": ["pull-up bar"],
        "difficulty": 4
    },
    {
        "name": "Lunges",
        "muscle_groups": ["quadriceps", "hamstrings", "glutes"],
        "equipment": [],
        "difficulty": 3
    },
    {
        "name": "Plank",
        "muscle_groups": ["core"],
        "equipment": [],
        "difficulty": 2
    },
    {
        "name": "Deadlift",
        "muscle_groups": ["back", "glutes", "hamstrings"],
        "equipment": ["barbell", "weights"],
        "difficulty": 5
    },
    {
        "name": "Shoulder Press",
        "muscle_groups": ["shoulders", "triceps"],
        "equipment": ["dumbbell"],
        "difficulty": 3
    },
    {
        "name": "Leg Press",
        "muscle_groups": ["quadriceps", "hamstrings", "glutes"],
        "equipment": ["leg press machine"],
        "difficulty": 3
    }
]


def get_user_input():
    print("Welcome to the Personalized Workout Plan Generator!")

    current_fitness = input("What is your current fitness level (beginner/intermediate/advanced)? ").lower()
    while current_fitness not in ["beginner", "intermediate", "advanced"]:
        current_fitness = input("Please enter a valid fitness level (beginner/intermediate/advanced): ").lower()

    weekly_availability = int(input("How many days per week are you available to work out? "))
    while weekly_availability < 1 or weekly_availability > 7:
        weekly_availability = int(input("Please enter a number between 1 and 7: "))

    print("\nWhat are your fitness goals? (select all that apply)")
    print("1. Build muscle")
    print("2. Lose weight")
    print("3. Improve endurance")

    goal_options = [1, 2, 3]
    user_goals = []
    while True:
        goal = input("Enter the number of your goal (or 'done' to finish): ")
        if goal.lower() == "done":
            if not user_goals:
                print("Please select at least one goal.")
                continue
            break
        elif goal.isdigit() and int(goal) in goal_options:
            user_goals.append(int(goal))
        else:
            print("Invalid input, please try again.")

    return current_fitness, weekly_availability, user_goals


def determine_exercises(current_fitness, user_goals, exercise_database):
    difficulty_ranges = {
        "beginner": (1, 3),
        "intermediate": (2, 4),
        "advanced": (3, 5)
    }

    goal_muscle_groups = {
        1: ["chest", "back", "shoulders", "biceps", "triceps", "quadriceps", "hamstrings", "glutes"],
        2: ["quadriceps", "hamstrings", "glutes", "core", "back"],
        3: ["quadriceps", "hamstrings", "glutes", "core", "back", "shoulders"]
    }

    min_difficulty, max_difficulty = difficulty_ranges[current_fitness]

    target_muscle_groups = set()
    for goal in user_goals:
        target_muscle_groups.update(goal_muscle_groups[goal])

    scored_exercises = []
    for exercise in exercise_database:
        if min_difficulty <= exercise['difficulty'] <= max_difficulty:
            score = 0
            for muscle_group in exercise['muscle_groups']:
                if muscle_group in target_muscle_groups:
                    score += 1
            if score > 0:
                scored_exercises.append((exercise, score))

    scored_exercises.sort(key=lambda x: x[1], reverse=True)

    return [exercise for exercise, _ in scored_exercises[:10]]


def generate_workout_plan(current_fitness, weekly_availability, user_goals, exercise_database):
    workout_plan = []

    suitable_exercises = determine_exercises(current_fitness, user_goals, exercise_database)

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
    print("\nYour Personalized Workout Plan:")
    for day, exercises in enumerate(workout_plan, start=1):
        print(f"\nDay {day}:")
        for exercise in exercises:
            print(
                f"- {exercise['name']}: {exercise['sets']} sets of {exercise['reps']} reps, {exercise['rest']} seconds rest")


# Main program
if __name__ == "__main__":
    current_fitness, weekly_availability, user_goals = get_user_input()
    workout_plan = generate_workout_plan(current_fitness, weekly_availability, user_goals, exercise_database)
    display_workout_plan(workout_plan)
