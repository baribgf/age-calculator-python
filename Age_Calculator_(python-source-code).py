from calendar import monthrange
import datetime
from random import randint
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class AgeCalc:
    def __init__(self, master=tk.Tk):
        self.master = master
        self.master.title("Age Calculator")
        self.master.resizable(0, 0)
        try:
            self.master.iconbitmap("app-icon.ico")
        except tk.TclError:
            pass

        # build ui
        self.frame1 = tk.Frame(master, height=200, width=200)
        self.frame1.pack(side='top')

        self.lbl_title = tk.Label(self.frame1, font="{@Microsoft JhengHei} 12 {}", text="----------------\nAge Calculator\n----------------")
        self.lbl_title.grid(column=0, columnspan=3, row=0)

        self.lblfrm_collect = tk.LabelFrame(self.frame1, font="{@Microsoft JhengHei} 8 {}", height=50, text=" Set your age (DD/MM/YYYY)", width=220)
        self.lblfrm_collect.grid(column=0, columnspan=3, pady=4, row=1)
        self.lblfrm_collect.grid_propagate(0)
        self.lblfrm_collect.grid_anchor("center")

        self.entry_day = ttk.Entry(self.lblfrm_collect, font="{Microsoft} 10 {}", justify="center", width=6)
        self.entry_day.grid(column=0, row=0)

        self.entry_month = ttk.Entry(self.lblfrm_collect, font="{Microsoft} 10 {}", justify="center", width=6)
        self.entry_month.grid(column=1, padx=4, row=0)

        self.entry_year = ttk.Entry(self.lblfrm_collect, font="{Microsoft} 10 {}", justify="center", width=8)
        self.entry_year.grid(column=2, row=0)

        self.btn_submit = ttk.Button(self.frame1, text="Submit", command=self.calc)
        self.btn_submit.grid(column=0, columnspan=2, padx=8, pady=4, row=2, sticky="w")

        self.btn_clear = ttk.Button(self.frame1, text="Clear", command=self.clear)
        self.btn_clear.grid(column=1, row=2)

        self.lblfrm_result = tk.LabelFrame(self.frame1, font="{@Microsoft JhengHei} 9 {}", height=100, text=" Result ", width=240)
        self.lblfrm_result.grid(column=0, columnspan=3, padx=8, row=3)
        self.lblfrm_result.pack_propagate(0)

        self.lbl_result = tk.Label(self.lblfrm_result, font="{@Microsoft JhengHei} 9 {}", text="Your result here")
        self.lbl_result.pack(expand="true", fill="both", side="top")

        self.btn_exit = ttk.Button(self.frame1, text="Exit", command=self.master.destroy)
        self.btn_exit.grid(columnspan=2, padx=8, pady=8, sticky="w")

        self.btn_about = ttk.Button(self.frame1, text="About", command=lambda:messagebox.showinfo("About", "Developed by: Bari BGF\nE-mail: bougafa.005@gmail.com"))
        self.btn_about.grid(column=1, columnspan=2, padx=8, pady=8, row=4, sticky="e")

        # Main widget
        self.mainwindow = self.frame1

    def calc(self):
        try:
            days = None
            months = None
            years = datetime.datetime.now().year-int(self.entry_year.get())
            
            if datetime.datetime.now().day < int(self.entry_day.get()):
                days = monthrange(int(self.entry_year.get()), int(self.entry_month.get()))[1] - abs(datetime.datetime.now().day-int(self.entry_day.get()))
            else:
                days = datetime.datetime.now().day-int(self.entry_day.get())

            if datetime.datetime.now().month < int(self.entry_month.get()):
                months = 12 - int(self.entry_month.get()) + datetime.datetime.now().month
            else:
                months = datetime.datetime.now().month - int(self.entry_month.get())

            if datetime.datetime.now().day < int(self.entry_day.get()):
                months-=1
            if datetime.datetime.now().month < int(self.entry_month.get()):
                years-=1

            if years<0 or months<0 or not 0<int(self.entry_month.get())<=12 or not 0<int(self.entry_day.get())<=monthrange(int(self.entry_year.get()), int(self.entry_month.get()))[1]:
                raise ValueError

            self.lbl_result["text"] = f"Your age is:\n{years} Years, {months} months, and {days} days."
        except ValueError:
            self.lbl_result["text"] = "You entered invalid data !"

    def clear(self):
        self.entry_year.delete(0, tk.END)
        self.entry_month.delete(0, tk.END)
        self.entry_day.delete(0, tk.END)
        self.lbl_result["text"] = "Your result here"

    def run(self):
        self.mainwindow.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = AgeCalc(root)
    app.run()
