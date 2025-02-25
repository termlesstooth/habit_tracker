from datetime import date, timedelta

class Habit:
    """models a habit"""
    def __init__(self, name: str, description:str, frequency:str):
        self.name = name
        self.description = description
        self.frequency = frequency
        self.start_date = date.today()
        self.current_streak = 0
        self.completed_today = False
        self.completion_log = {}

    def update_log(self):
        """updates the completion log"""
        self.completion_log[date.today()] = self.completed_today

    def mark_completed(self):
        """marks habit as completed for the day"""
        self.completed_today = True
        self.update_log()
        self.update_streak()

    def update_streak(self):
        """update habit streak"""
        if self.completion_log.get(date.today() - timedelta(days=1), False) and self.completed_today: self.current_streak += 1
        elif not self.completed_today: self.current_streak = 0
        elif not self.completion_log.get(date.today() - timedelta(days=1), False) and self.completed_today: self.current_streak = 1

    def get_streak(self):
        """returns your current streak for that habit"""
        return self.current_streak


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
                habit.mark_completed
                break
    
    def daily_reset(self):
        """Resets daily flags for all habits at the start of a new day."""
        for habit in self.habits:
            habit.completed_today = False
    
    def generate_report(self):
        """Generates a report summarizing all tracked habits."""
        report = "Habit Report:\n"
        for habit in self.habits:
            report += f"{habit.name}: Current Streak = {habit.get_streak()}\n"
        return report

dsa = Habit("Data Structures and Algorithms", "Read/Work on exercises from DSA in Python book", "d")
dsa.mark_completed()
dsa.update_streak()
print(f"For your {dsa.name} habit, you have completed it {dsa.get_streak()} day(s) in a row!")

habit_tracker = HabitTracker()
habit_tracker.add_habit(dsa)
print(habit_tracker.generate_report())