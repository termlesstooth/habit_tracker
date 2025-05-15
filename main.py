import argparse, json, logging
from models.classes import Habit, HabitTracker
#from visualization.habit_charts import plot_rolling_success_rate
from datetime import date

logging.basicConfig(
    level=logging.DEBUG,
    filename="log.log",
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s"
)


# get a logger object
logger = logging.getLogger(__name__)  

# read in habits
logger.info("Reading habit_tracker_object.json file")
try:
    with open('data/habit_tracker_object.json', 'r') as f:
        data = json.load(f)
    logger.info("Succsessfully read habit_tracker_object.json")
except FileNotFoundError:
    logger.warning("File not found")
except  Exception:
    logger.exception("Unexpected error while reading habit_tracker_object.json")

# store habits in habit tracker object
logger.info("Creating HabitTracker object")
all_habits = HabitTracker()
# TODO: can probably store the for loop as a method
for habit in data:
    all_habits.add_habit(Habit.from_dict(habit))
logger.info("Added habits to HabitTracker object")

parser = argparse.ArgumentParser(description="Interact with your habit tracker!")
parser.add_argument("-mc", "--habits", nargs='*', help="The habits you want to mark as completed for the day")
parser.add_argument("-a", "--add", help = "A habit you want to add to the habit tracker")
args = parser.parse_args()

# mark habits that user inputs as completed for the day
if args.habits:
    logger.info("Marking habit as complete")
    try:
        for habit in args.habits:
            all_habits.mark_habit_completed(habit)
        logger.info("Marked habits as completed")
    except Exception:
        logger.exception(f"Unexpected error occured while marking a habit as complete")

if args.add:
    try:
        all_habits.add_habit(Habit(args.add))
    except Exception as e:
        print(f"Unexpected error: {e}")

# TODO: Add in description as well, add a method to update habit description too

#print(all_habits.generate_report())

#TODO: Fix habit streak function

all_habits.generate_daily_habit_to_do()

with open('data/habit_tracker_object.json', 'w') as f:
    json.dump(all_habits.convert_to_list_of_dicts(), f, indent=4)

# TODO: Add argparser arguemnts to add habits, display habits, etc. 
# TODO: Need to fix Habit Report, current streak should not be 1 if I didn't do it for the day
# TODO: Need to write the habit tracker object to storage. Is the best way to do this with JSON Data or CSV. Complete that.
# TODO: Need to make it so that if I miss a day it automatically updates the log\

