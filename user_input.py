import pygame as pg
import random
import tkinter as tk


def car_settings():
    root = tk.Tk()
    root.title("Traffic settings")
    root.grid()

    car_amount = tk.IntVar()
    front_time_stopped = tk.IntVar()
    time_simulation = tk.IntVar()
    file_name = tk.StringVar()
    tk.Label(root, text='Number of cars:').grid(column=0, row=0)
    tk.Entry(root, bd=3, textvariable=car_amount).grid(column=1, row=0)
    tk.Label(root, text='Time front car is stopped:').grid(column=0, row=1)
    tk.Entry(root, bd=3, textvariable=front_time_stopped).grid(column=1, row=1)
    tk.Label(root, text='Time of sim run:').grid(column=0, row=2)
    tk.Entry(root, bd=3, textvariable=time_simulation).grid(column=1, row=2)
    #  tk.Label(root, text='Save file name:').grid(column=0, row=3)
    #  tk.Entry(root, bd=3, textvariable=file_name).grid(column=1, row=3)
    tk.Button(root, text="save & quit", command=root.destroy).grid(column=1, row=4)

    root.mainloop()
    saved = [car_amount.get(), front_time_stopped.get(), time_simulation.get(), file_name.get()]
    return saved
