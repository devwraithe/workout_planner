# Exercise Database
exercise_database = [
    {
        "name": "Plank",
        "muscle_groups": ["core"],
        "equipment": [],
        "difficulty": 2
    },
    {
        "name": "Hammer Curl",
        "muscle_groups": ["biceps", "forearms"],
        "equipment": ["dumbbell"],
        "difficulty": 2
    },
    {
        "name": "Incline Dumbbell Press",
        "muscle_groups": ["chest", "shoulders", "triceps"],
        "equipment": ["dumbbell"],
        "difficulty": 3
    },
    {
        "name": "Bulgarian Split Squat",
        "muscle_groups": ["quadriceps", "glutes", "hamstrings"],
        "equipment": ["dumbbell"],
        "difficulty": 4
    },
    {
        "name": "Pull-ups",
        "muscle_groups": ["back", "biceps"],
        "equipment": ["pull-up bar"],
        "difficulty": 4
    },
    {
        "name": "Dips",
        "muscle_groups": ["chest", "shoulders", "triceps"],
        "equipment": ["parallel bars"],
        "difficulty": 3
    },
    {
        "name": "Deadlift",
        "muscle_groups": ["back", "glutes", "hamstrings"],
        "equipment": ["barbell", "weights"],
        "difficulty": 5
    },
    {
        "name": "Squat",
        "muscle_groups": ["quadriceps", "glutes", "hamstrings"],
        "equipment": ["barbell", "weights"],
        "difficulty": 4
    },
    {
        "name": "Arnold Press",
        "muscle_groups": ["shoulders", "triceps"],
        "equipment": ["dumbbell"],
        "difficulty": 4
    },
    {
        "name": "Bicep Curl",
        "muscle_groups": ["biceps"],
        "equipment": ["dumbbell"],
        "difficulty": 2
    },
    {
        "name": "Step-ups",
        "muscle_groups": ["quadriceps", "glutes", "hamstrings"],
        "equipment": ["bench", "dumbbells"],
        "difficulty": 3
    },
    {
        "name": "Russian Twists",
        "muscle_groups": ["core", "obliques"],
        "equipment": ["medicine ball"],
        "difficulty": 3
    },
    {
        "name": "Leg Extension",
        "muscle_groups": ["quadriceps"],
        "equipment": ["leg extension machine"],
        "difficulty": 2
    },
    {
        "name": "Barbell Bench Press",
        "muscle_groups": ["chest", "shoulders", "triceps"],
        "equipment": ["barbell", "weights"],
        "difficulty": 3
    },
    {
        "name": "Lunges",
        "muscle_groups": ["quadriceps", "hamstrings", "glutes"],
        "equipment": [],
        "difficulty": 3
    },
    {
        "name": "Sumo Deadlift",
        "muscle_groups": ["back", "glutes", "hamstrings"],
        "equipment": ["barbell", "weights"],
        "difficulty": 5
    },
    {
        "name": "Chin-ups",
        "muscle_groups": ["back", "biceps"],
        "equipment": ["pull-up bar"],
        "difficulty": 4
    },
    {
        "name": "Leg Press",
        "muscle_groups": ["quadriceps", "hamstrings", "glutes"],
        "equipment": ["leg press machine"],
        "difficulty": 3
    },
    {
        "name": "Shoulder Press",
        "muscle_groups": ["shoulders", "triceps"],
        "equipment": ["dumbbell"],
        "difficulty": 3
    },
    {
        "name": "Push-ups",
        "muscle_groups": ["chest", "shoulders", "triceps"],
        "equipment": [],
        "difficulty": 2
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
    1: ["core", "shoulders", "chest", "biceps", "triceps", "quadriceps", "hamstrings", "glutes", "back"],
    2: ["core", "biceps", "quadriceps", "hamstrings", "glutes", "chest", "shoulders", "triceps", "back"],
    3: ["chest", "shoulders", "triceps", "quadriceps", "hamstrings", "glutes", "core", "back", "obliques", "forearms"],
    4: ["quadriceps", "glutes", "hamstrings", "shoulders", "triceps", "back", "biceps"],
    5: ["back", "glutes", "hamstrings"]
}
