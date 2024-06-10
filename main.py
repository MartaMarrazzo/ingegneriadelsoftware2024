# main.py
import tkinter as tk

from Controller.LoginController import LoginController
from View.Home.HomepageView import HomePageView


def main():
    print("Benvenuto nel mio nuovo progetto Python!")

if __name__ == "__main__":
    root = tk.Tk()
    controller = LoginController(None)  # Initially, view is None
    app = HomePageView(root, controller)
    controller.view = app  # Now that view is created, assign it to controller
    root.mainloop()