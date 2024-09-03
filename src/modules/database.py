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

# Difficulty Ranges
difficulty_ranges = {
        "beginner": (1, 3),
        "intermediate": (2, 4),
        "advanced": (3, 5)
    }

# Muscle Group Database
difficulty_muscle_groups = {
    1: ["chest", "back", "shoulders", "biceps", "triceps", "quadriceps", "hamstrings", "glutes"],
    2: ["quadriceps", "hamstrings", "glutes", "core", "back"],
    3: ["quadriceps", "hamstrings", "glutes", "core", "back", "shoulders"]
}
