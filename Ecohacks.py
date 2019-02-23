""" Challenge 2 -

Code to ask the user about the choices about garbage disposal that he has.
"""
from datetime import date
from datetime import datetime
from datetime import timedelta


class Activity:
    """ The every day activities that the user has created for helping out the
    environment.

    === Attributes ===
    name: the name of the activity
    tip: tips regarding the activity that is going on
    act_date: the date since the user has been maintaining the streak
    """
    def __init__(self, n: str) -> None:
        """ Initializes the class Activity.
        """
        self.name = n
        self.act_date = datetime.now()

    def generate_a_tip(self) -> str:
        """ Generates a tip for the user to be printed for the particular tip.
        """
        pass


class StreakManager:
    """ Creates streaks of the activities that the user has generated pr wish to
    add to his check list system.

    === Attributes ===
    _streaks: dict for the activity and the number of days that the user has
        completed. The value is [date, days for the streak.
    today: the current date.
    """
    _streaks: dict
    today: datetime.date

    def __init__(self) -> None:
        """ Initializes the class.
        """
        self._streaks = {}
        d = datetime.now()
        self.today = date(d.year, d.month, d.day)

    def add_activity(self, a: Activity) -> None:
        """ Adds the activity to the main dictionary"""
        self._streaks[a] = [self.today, 0]

    def update_today(self) -> None:
        """ Updates the date of the whole system.
        """
        d = datetime.now()
        self.today = date(d.year, d.month, d.year)

    def calculate_streak(self) -> None:
        """ Calculates the streak and mutates the activity in the streaks master
        dictionary.
        It updates the dates for every day

        * Mutates the self._streaks

        Precondition: this function is called everyday
        """
        for i in self._streaks:
            new_date = self.today + timedelta(days=-1)
            # in a continuous streak
            if i[1] == new_date:
                i[1] += 1
            else:
                i[1] = 0


class EcoPoints:
    """ Calculates the EcoPoints that the user has.

    ===Attributes===
    points: the eco points that the user has.
    """
    points: int

    def __init__(self) -> None:
        """ Initializes the class.
        """
        self.points = 0

    def add_points(self, garbage_type: str) -> None:
        """ Adds the points.

        garbage types-

        REUSABLE
        DEGRADABLE
        NON-DEGRADABLE
        """
        if garbage_type == "REUSABLE":
            self.points += 15
        elif garbage_type == "DEGRADABLE":
            self.points += 5
        elif garbage_type == "NON-DEGRADABLE":
            self.points += 5
        else:
            pass


if '__main__' == __name__:
    pass
