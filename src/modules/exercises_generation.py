from src.modules.database import difficulty_ranges, difficulty_muscle_groups


def generate_exercises(current_fitness, user_goals, exercise_database):
    goal_muscle_groups = difficulty_muscle_groups

    (min_difficulty, max_difficulty) = difficulty_ranges[current_fitness]

    target_muscle_groups = set()
    for goal in user_goals:
        target_muscle_groups.update(goal_muscle_groups[goal])

    generated_exercises = []
    for exercise in exercise_database:
        if min_difficulty <= exercise['difficulty'] <= max_difficulty:
            score = 0
            for muscle_group in exercise['muscle_groups']:
                if muscle_group in target_muscle_groups:
                    score += 1
            if score > 0:
                generated_exercises.append((exercise, score))

    generated_exercises.sort(key=lambda x: x[1], reverse=True)

    return [exercise for exercise, _ in generated_exercises[:10]]
