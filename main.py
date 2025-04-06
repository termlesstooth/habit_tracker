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
parser.add_argument("-H", "--habits", nargs='*', help="The habits you want to mark as completed for the day")
args = parser.parse_args()

# mark habits that user inputs as completed for the day
if args.habits:
    try:
        for habit in args.habits:
            all_habits.mark_habit_completed(habit)
    except Exception as e:
        print(f"Unexpected error: {e}")

print(all_habits.generate_report())

#TODO: Fix habit streak function


with open('data/habit_tracker_object.json', 'w') as f:
    json.dump(all_habits.convert_to_list_of_dicts(), f, indent=4)

# TODO: Need to fix Habit Report, current streak should not be 1 if I didn't do it for the day
# TODO: Need to write the habit tracker object to storage. Is the best way to do this with JSON Data or CSV. Complete that.
# TODO: Need to make it so that if I miss a day it automatically updates the log