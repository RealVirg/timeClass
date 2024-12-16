import time


class GameTime:
    def __init__(self) -> None:
        self.days = 0
        self.hours = 0
        self.minutes = 0
        
        self.update_speed = 30

        self.current_name_day = 0

        self.day_list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    
    def get_current_name_day(self):
        return self.day_list[self.current_name_day]
    
    def update(self):
        self.minutes += self.update_speed
        added_hours = self.minutes // 60
        self.minutes = self.minutes % 60
        self.hours += added_hours
        self.days += self.hours // 24
        self.hours = self.hours % 24
        self.current_name_day = self.days % 7

    def show_time(self):
        return f"{self.get_current_name_day()} {self.hours}:{self.minutes:02d}"
