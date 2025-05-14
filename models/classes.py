from datetime import date, timedelta, datetime
import logging

logger = logging.getLogger(__name__)

#TODO: Add in a time metric so I can track how much time I spent each day on things 
class Habit:
    """models a habit"""
    def __init__(self, name: str, description = "", frequency = "d", start_date=None, current_streak=0, completed_today=False, completion_log={}):
        self.name = name
        self.description = description
        self.frequency = frequency
        if not start_date:
            self.start_date = date.today()
        else:
            self.start_date = start_date
        self.current_streak = current_streak
        self.completed_today = completed_today
        self.completion_log = completion_log

    def update_log(self):
        """updates the completion log"""
        self.completion_log[str(date.today())] = self.completed_today # TODO: Is making the key a string here bad practice? should I do this when I write to JSON. Chat GPT says date objects arent json serializable. Investigate

    def mark_completed(self):
        """Marks habit as completed for the day."""
        self.completed_today = True
        logger.info(f"Marked [{self.name}] as completed")
        print(f"\n🎉 Congrats on completing {self.name} for the day!")
        self.update_log()
        self.update_streak()

    def update_streak(self):
        # TODO: need to update this so it can run every day
        """update habit streak"""
        # if user didn't complete yesterday and today:
        if not self.completion_log.get(date.today() - timedelta(days=1)) and not self.completed_today:
            self.current_streak = 0
        # if user completed yesterday and today:
        elif self.completion_log.get(date.today() - timedelta(days=1), False) and self.completed_today: self.current_streak += 1
        # if user just completed today
        elif self.completed_today:
            self.current_streak = 1


    def get_streak(self):
        """returns your current streak for that habit"""
        return self.current_streak
    
    def display_log(self):
        """Displays the completion log for that habit."""
        return self.completion_log

    def to_dict(self):
        data = {
            "name": self.name,
            "description": self.description,
            "frequency": self.frequency,
            "start_date": str(self.start_date), # ensure it's a string for JSON compatability
            "current_streak": self.current_streak,
            "completed_today": self.completed_today,
            "completion_log": self.completion_log
        }
        return data
    
    # TODO: may want to convert start_date back toa  date object if it is stored as a string
    @classmethod
    def from_dict(cls,data):
        """Create a habit instance from a dictionary"""
        return cls(**data)


class HabitTracker:
    """manages a collection of Habit objects for tracking daily habits"""
    def __init__(self):
        self.habits = [] # list to store habit instances

    def add_habit(self, habit):
        """Adds a new habit to the tracker"""
        self.habits.append(habit)

    def remove_habit(self, habit_name):
        """Removes a habit by its name"""
        self.habits = [habit for habit in self.habits if habit.name != habit_name]

    def mark_habit_completed(self, habit_name):
        """Marks a specific habit as completed for today"""

        for habit in self.habits:
            if habit.name == habit_name:
                habit.mark_completed()
    
    def daily_reset(self):
        """Resets daily flags for all habits at the start of a new day."""
        for habit in self.habits:
            habit.completed_today = False
    
    def generate_report(self):
        """Generates a report summarizing all tracked habits."""
        report = "Habit Report:\n"
        for habit in self.habits:
            report += f"{habit.name}: Log = {habit.display_log()}\n"
        return report
    
    def convert_to_list_of_dicts(self):
        """Convert the list of habit objects to a list of dictionaries."""
        data = []
        for habit in self.habits:
            data.append(habit.to_dict())
        return data
    
    def update_streaks(self):
        for habit in self.habits:
            habit.update_streak()

    def generate_daily_habit_to_do(self):
        """Generates a user's habit to-do list for the day."""
        to_do_list = []
        completed_list = []
        for habit in self.habits:
            last_logged_str = next(reversed(habit.completion_log))
            last_logged_date = datetime.strptime(last_logged_str, "%Y-%m-%d").date()
            if last_logged_date != date.today(): # check if a log for that habit exists for today
                to_do_list.append(habit.name)
                logging.info("Added a habit to the to-do list")
            else:
                completed_list.append(habit.name)
                logging.info("Added a habit to the completed list")


        formatted_date = date.today().strftime("%A the %d of %B, %Y")
        # TODO: Add a function to reference current time and write the appropriate greeting. 
        print(f"\n🌞 Good morning, Jack! It's {formatted_date}.")
        if to_do_list:
            print("📝 Here's your habit hit list for today:")
            for habit in to_do_list:
                print(f"\t⭕ {habit}")
        if completed_list:
            print("💪 You have already completed:")
            for habit in completed_list:
                print(f"\t✅ {habit}")
        else:
            print("🎉 All habits complete - you're crushing it today!")
                
