# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal

goal_set = False

def log_workout(workout_type, duration):
    workouts.append(workout_type)
    workouts.append(duration)
    return "\n" + f'Exercise ({workout_type}) added with duration {duration} minutes.' + '\n'

def log_calorie_intake(calories_consumed):
    calories.append(calories_consumed)
    return "\n" + f'{calories_consumed} calories consumed.' + '\n'

def view_progress():
    global workout_time, total_kcal
    workout_time = sum(filter(lambda x: type(x) == int, workouts))
    total_kcal = sum(calories)
    return "\n" + f"Total workout time: {workout_time} minutes." + "\n" + f"Total calories: {total_kcal}" + '\n'

def reset_progress():
    global workout_goal, calorie_goal, workouts, calories, workout_time, total_kcal, goal_set
    workouts = []
    calories = []
    workout_goal = 0
    calorie_goal = 0
    workout_time = 0
    total_kcal = 0
    goal_set = False
    return "\n" + 'Progress reset!' + '\n'

def set_daily_goals(workout_minutes, calorie_limit):
    global workout_goal, calorie_goal, goal_set
    workout_goal += workout_minutes
    calorie_goal += calorie_limit
    goal_set = True
    return "\n" + f'Goal set! Workout goal is {workout_minutes} minutes. Calories goal is {calorie_limit} calories or under.' + '\n' + 'Good luck!' + '\n'

def encouragement_system():
    if workout_time == workout_goal:
        workout_result =  f'You have met your workout goal!'
    elif workout_time > workout_goal:
        workout_result = f'You have surpassed your workout goal by {workout_time - workout_goal} minutes.'
    else:
        workout_result = f'You need to exercise for {workout_goal - workout_time} more minutes to reach your goal!'

    if total_kcal == calorie_goal:
        kcal_result = f'You have met your calorie goal!'
    elif total_kcal > calorie_goal:
        kcal_result = f'You have surpassed your calorie goal by {total_kcal - calorie_goal} calories.'
    else:
        kcal_result = f'You can eat {calorie_goal - total_kcal} more calories.'
    return 'Workout:' + '\n' + workout_result + '\n' + '\n' + 'Calories' + '\n' + kcal_result + '\n'

def main():
    """
    Main function to interact with the user.
    """
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        # Prompt user for their choice
        choice = input("\nEnter your choice: ")

        if choice == '1':
            workout_type = input('\n' + 'Workout type: ')
            workout_duration = int(input('Workout duration: '))
            print(log_workout(workout_type, workout_duration))

        elif choice == '2':
            user_kcal = int(input('\n' +'Calories consumed: '))
            print(log_calorie_intake(user_kcal))

        elif choice == '3':
            print(view_progress())
            if goal_set:
                print(encouragement_system())
        elif choice == '4':
            print(reset_progress())

        elif choice == '5':
            minutes_goal = int(input('\n' + 'What is your workout minutes goal? '))
            kcal_goal = int(input('What is your calorie intake goal? '))
            print(set_daily_goals(minutes_goal, kcal_goal))

        elif choice == '6':
            # Print a goodbye message and break the loop
            print('\n' + "Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print('\n' + "Invalid choice, please try again.")


if __name__ == "__main__":
    main()