import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title("League Tier List")
root.geometry("600x600")
champs = []

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

canvas = Canvas(main_frame)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = tk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

second_frame = Frame(canvas)
canvas.create_window((0, 0), window=second_frame, anchor="nw")
images = []


tk.Label(second_frame,
          text="League of Legends Tier List",
          font=("Times New Roman", 15)).grid(column=1, row=0, pady=20, padx=100)


for i in range(45):
    images.append(PhotoImage(file=f"images/champ{i}.png"))
    Label(second_frame, image=images[i], width=60, height=60).grid(pady=20, padx=10)


root.mainloop()

