import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("Jungle Tier List")
root.geometry("800x600")
champs = []


tk.Label(root,
          text="League of Legends Tier List",
          font=("Times New Roman", 15)).grid(column=0, row=0)

canvas = Canvas(root, width=300, height=300)
canvas.grid(column=0, row=1)
img = PhotoImage(file="images/champ1.png")
canvas.create_image(20, 20, anchor=NW, image=img)

root.mainloop()