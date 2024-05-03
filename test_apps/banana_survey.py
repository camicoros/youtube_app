"""
Banana survey
This program asks about bananas
author: D.D. Saushkin
"""
import tkinter as tk


root = tk.Tk()
# set title for window
root.title("Banana interest survey")
# set size and position for window
# 300px from the left and 300px from the top
root.geometry("640x480+300+300")
# set window can't be resizable horizontally and vertically
root.resizable(False, False)

# fg - text color
title = tk.Label(
    root,
    text="Please take the survey",
    font=("Arial 16 bold"),
    bg="brown",
    fg="#FF0"
)

name_var = tk.StringVar(root)
name_label = tk.Label(root, text="What's your name?")
name_inp = tk.Entry(root, textvariable=name_var)

eater_var = tk.BooleanVar()
eater_inp = tk.Checkbutton(
    root,
    variable=eater_var,
    text="Check this box if you eat bananas"
)

num_var = tk.IntVar(value=3)
num_label = tk.Label(
    root,
    text="How many bananas do you eat per day?"
)
num_inp = tk.Spinbox(root, textvariable=num_var, from_=0, to=1000, increment=1)

color_var = tk.StringVar(value="Any")
color_label = tk.Label(
    root,
    text="What's the best color for a banana?"
)
color_choices = (
    "Any",
    "Green",
    "Green-Yellow",
    "Yellow",
    "Brown Spotted",
    "Black"
)
color_inp = tk.OptionMenu(root, color_var, *color_choices)

plantain_var = tk.BooleanVar()
plantain_label = tk.Label(root, text="Do you eat plantains?")
plantain_frame = tk.Frame(root)
plantain_yes_inp = tk.Radiobutton(plantain_frame, value=True, variable=plantain_var, text="Yes!")
plantain_no_inp = tk.Radiobutton(plantain_frame, value=False, variable=plantain_var, text="Eww, NO!")

banana_story_label = tk.Label(
    root,
    text="Write a story about bananas"
)
banana_story_inp = tk.Text(root, height=3)

submit_btn = tk.Button(root, text="Submit Survey")

output_var = tk.StringVar(value="")
output_line = tk.Label(
    root,
    textvariable=output_var,
    anchor="w",
    justify="left"
)


def on_submit():
    name = name_var.get()

    try:
        number = num_var.get()
    except tk.TclError:
        number = 10000

    color = color_var.get()
    banana_eater = eater_var.get()
    plantain_eater = plantain_var.get()

    # 1.0 means first character of the first line
    # from first to end
    story = banana_story_inp.get("1.0", tk.END)
    message = f"Thanks for taking the survey, {name}.\n"
    if not banana_eater:
        message += "Sorry you don't like bananas!\n"
    else:
        message += f"Enjoy your {number} {color} bananas!\n"
    if plantain_eater:
        message += "Enjoy your plantains!\n"
    else:
        message += "May you successfully avoid plantains!\n"
    if story.strip():
        message += f"Your banana story:\n{story}"

    output_var.set(message)


submit_btn.configure(command=on_submit)


title.grid(columnspan=2)

name_label.grid(row=1, column=0)
name_inp.grid(row=1, column=1)

eater_inp.grid(row=2, columnspan=2, sticky="we")

num_label.grid(row=3, sticky=tk.W)
num_inp.grid(row=3, column=1, sticky=(tk.W+tk.E))

color_label.grid(row=4, columnspan=2, sticky=tk.W, pady=10)
color_inp.grid(row=5, columnspan=2, sticky=tk.W, pady=10)

plantain_yes_inp.pack(side=tk.LEFT, fill=tk.X, ipadx=10, ipady=5)
plantain_no_inp.pack(side=tk.LEFT, fill=tk.X, ipadx=10, ipady=5)
plantain_label.grid(row=6, columnspan=2, sticky=tk.W)
plantain_frame.grid(row=7, columnspan=2, sticky=tk.W)

banana_story_label.grid(row=8, sticky=tk.W)
banana_story_inp.grid(row=9, columnspan=2, sticky="NSEW")

submit_btn.grid(row=99, columnspan=2)
output_line.grid(row=100, columnspan=2, sticky="NSEW")

root.columnconfigure(1, weight=1)
root.rowconfigure(99, weight=2)
root.rowconfigure(100, weight=1)

root.mainloop()
