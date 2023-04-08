from calendar import monthrange
import datetime
from random import randint
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

class AgeCalc:
    def __init__(self, master):
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

        self.lblfrm_collect = tk.LabelFrame(self.frame1, font="{@Microsoft JhengHei} 8 {}", height=50, text=" Enter your birthday (DD/MM/YYYY)", width=220)
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
        user_day = int(self.entry_day.get())
        user_month = int(self.entry_month.get())
        user_year = int(self.entry_year.get())
        month_days = monthrange(user_year, user_month)[1]

        days = None
        months = None
        years = datetime.datetime.now().year - user_year

        today = datetime.datetime.now().day
        this_month = datetime.datetime.now().month
        
        if today < user_day:
            days = month_days - abs(today - user_day)
        else:
            days = today - user_day

        if this_month < user_month:
            months = 12 - user_month + this_month
        else:
            months = this_month - user_month

        if today < user_day:
            months -= 1
        if this_month < user_month:
            years -= 1

        if years < 0 or months < 0 \
            or not 1 <= user_month <= 12 \
            or not 1 <= user_day <= month_days:
            self.lbl_result["text"] = "Invalid data entered!"
            return

        self.lbl_result["text"] = f"Your age is:\n{years} Years, {months} months, and {days} days."

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
