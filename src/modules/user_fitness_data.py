def get_user_fitness_data():
    print("\n>>> Personalized Workout Planner! <<<\n")

    # Fitness levels range from beginner to advanced
    fitness_levels = ["beginner", "intermediate", "advanced"]
    levels_text = "(Beginner, Intermediate or Advanced)"

    current_fitness = input(f"What is your current fitness level? {levels_text}: ").lower()
    while current_fitness not in fitness_levels:  # Validate the user input
        current_fitness = input(f"Please enter a valid fitness level {levels_text}: ").lower()

    weekly_availability = int(input("How many days are you available to workout in a week? "))
    while weekly_availability < 1 or weekly_availability > 7:
        weekly_availability = int(input("Please enter a number between 1 and 7: "))

    print("\nWhat are your fitness goals? (select all that apply)")
    print("1. Build muscle")
    print("2. Lose weight")
    print("3. Improve endurance")

    goal_options = [1, 2, 3]
    user_goals = []
    while True:
        selected_goal = input("Enter the number of your goal (or 'done' to proceed): ")
        if selected_goal.lower() == "done":
            if not user_goals:  # Check if user_goals is empty
                print("Please select at least one goal (1, 2, or 3).")
                continue  # Continue the loop to ask for a goal again
            break
        elif selected_goal.isdigit() and int(selected_goal) in goal_options:
            user_goals.append(int(selected_goal))   # Append the selected goal to user_goals
        else:
            print("Invalid input, please try again.")

    return current_fitness, weekly_availability, user_goals
