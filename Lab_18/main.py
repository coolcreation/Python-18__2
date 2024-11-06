#  Jeff Bohn
#  11/06/2024
#  Python Chapter 18 - GUI program
#  main.py


#############################################
############### Exercise 18-2 ###############
#############################################


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def show_error():
    messagebox.showerror("Error", "Must be a positive number only, try again!")

def validate(miles_driven, gallons_used, mpg):
    try:
        first = float(miles_driven.get())
        second = float(gallons_used.get())
        if first > 0 < second:
            numTotal = first / second
            mpg.set(round(numTotal, 2))
        else:
            show_error()
    except Exception as e:
        show_error()
        print("Error message is: ", e)


def main():
    root = tk.Tk()
    root.title("Miles Per Gallon Calculator")
    root.geometry("360x180")

    frame = ttk.Frame(root, padding="15 15 15 15")
    frame.grid(row=0, column=0)

    tk.Label(frame, text="Miles Driven:", font=("Arial", 13)).grid(row=1, column=1, sticky=tk.E)   
    tk.Label(frame, text="Gallons of Gas Used:", font=("Arial", 13)).grid(row=2, column=1, sticky=tk.E)

    tk.Label(frame, text="Miles Per Gallon:", font=("Arial", 13)).grid(row=3, column=1, sticky=tk.E)


    miles_driven = tk.StringVar()
    tk.Entry(frame, textvariable=miles_driven, width=13, font=("Arial", 13)).grid(row=1, column=2, columnspan=1)

    gallons_used = tk.StringVar()
    tk.Entry(frame, textvariable=gallons_used, width=13, font=("Arial", 13)).grid(row=2, column=2, columnspan=1)

    mpg = tk.StringVar()
    tk.Entry(frame, textvariable=mpg, width=11, font=("Arial", 14), state="readonly").grid(row=3, column=2, columnspan=1)

    tk.Button(frame, width=10, text="Calculate", command=lambda: validate(miles_driven, gallons_used, mpg), font=("Arial", 15), fg="white", bg="black").grid(row=5, column=2)

    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=4)

    root.mainloop()  # make window visible, allow events, code after all other statements
    
main()