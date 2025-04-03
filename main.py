import argparse, json
from models.classes import Habit, HabitTracker
from datetime import date

# read in habits
try:
    with open('data/habit_tracker_object.json', 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    print("File not found") 
except  Exception as e:
    print(f"Unexpected error: {e}")

# store habits in habit tracker object
all_habits = HabitTracker()
# TODO: can probably store the for loop as a method
for habit in data:
    all_habits.add_habit(Habit.from_dict(habit))

parser = argparse.ArgumentParser()
parser.add_argument("habit", help="the habit you want to mark as completed for the day")
args = parser.parse_args()

try:
    all_habits.mark_habit_completed(args.habit)
except Exception as e:
    print(f"Unexpected error: {e}")

print(all_habits.generate_report())
# design give input -habit and mark that habit as completed for the day

# all_habits.update_streaks()

# all_habits.mark_habit_completed("Work on Habit Tracker")
# all_habits. mark_habit_completed("Data Structures and Algorithms")

with open('data/habit_tracker_object.json', 'w') as f:
    json.dump(all_habits.convert_to_list_of_dicts(), f, indent=4)

# TODO: Need to fix Habit Report, current streak should not be 1 if I didn't do it for the day

# # write a new habit
# python_dsa = Habit("Data Structures and Algorithms", "Solve Data Structures and Algorithms Python Problems","d")
# all_habits.add_habit(python_dsa)


# TODO: Need to write the habit tracker object to storage. Is the best way to do this with JSON Data or CSV. Complete that.
# TODO: Need to make it so that if I miss a day it automatically updates the log