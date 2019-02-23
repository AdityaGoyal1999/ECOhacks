""" The interactive visualizer for the Ecohacks2019.
"""
from tkinter import *
from Ecohacks import Activity, StreakManager
import pygame
# import tkMessageBox


# class Visualizer:
#     """
#     === Public Attributes ===
#     r: the tkinter object for the visual interface of the program
#     """
#     def __init__(self) -> None:
#         """Initialize this visualization.
#         """
#         self.r = Tk()

# def func():
#     top = tkinter.Tk()
#
#
# if "__main__" == __name__:
#     func()

class MyFirstGUI:
    """

    """
    def __init__(self, master):
        self.master = master
        master.title("EcoBro")

        self.label = Label(master, text="Welcome to EcoBro")
        self.label.pack()

        self.greet_button = Button(master, text="EcoPoints Calculator", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Eco Streaks", command=self.personal_streaks)
        self.close_button.pack()

        self.exit_button = Button(master, text="Quit Application", command=master.quit)
        self.exit_button.pack()
        self.streaks = StreakManager()

    def greet(self):
        print("Welcome to EcoPoints generator.")
        new_root = Tk()
        label = Label(new_root, text="Welcome to the EcoPoints generates.")
        label.pack()
        # var = StringVar()
        # print("This is the second window")
        # var.set("Welcome to your step of saving the environment.")
        # label = Message(new_root, textvariable=var, relief=RAISED)
        # label.pack()
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
