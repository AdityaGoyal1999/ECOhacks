""" The interactive visualizer for the Ecohacks2019.
"""
from tkinter import *
from Ecohacks import Activity, StreakManager, EcoPoints
import pygame


class Visualizer:
    """

    """
    def __init__(self, master):
        self.master = master
        master.title("EcoBro")

        self.label = Label(master, text="Welcome to EcoBro")
        self.label.pack()

        self.greet_button = Button(master, text="EcoPoints Calculator", command=self.points)
        self.greet_button.pack()

        self.close_button = Button(master, text="Eco Streaks", command=self.personal_streaks)
        self.close_button.pack()

        self.exit_button = Button(master, text="Quit Application", command=master.quit)
        self.exit_button.pack()
        self.streaks = StreakManager()

    def points(self):
        print("Welcome to EcoPoints generator.")
        new_root = Tk()
        label = Label(new_root, text="Welcome to the EcoPoints generates.")
        label.pack()
        e = EcoPoints()
        new_root1 = Tk()
        label1 = Label(new_root1, text="Enter the type of waste you have discarded properly.")
        label1.pack()
        w = StringVar()
        var = Entry(new_root1, text="Enter waste type", textvariable=w)
        var.pack()
        e.add_points(w)

        new_root2 = Tk()
        label = Label(new_root2, text=str(e.get_points()))
        label.pack()
        new_root2.mainloop()
        new_root1.mainloop()
        new_root.mainloop()

    def create_activity(self) -> None:
        """ Creates an activity for the user.
        """
        new_root = Tk()
        label = Label(new_root, text="Enter the activity you want to keep doing")
        label.pack()
        w = StringVar()
        e = Entry(new_root, text="Enter an activity", textvariable=w)
        e.pack()
        self.streaks.add_activity(w.get())
        new_root.mainloop()

    def personal_streaks(self):
        """ Manages the streaks.
        """
        print("Welcome to EcoPoints")
        new_root = Tk()
        label = Label(new_root, text="Welcome to EcoStreak")
        button1 = Button(new_root, text="Create Activity", command=self.create_activity)
        button1.pack()
        label.pack()



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
