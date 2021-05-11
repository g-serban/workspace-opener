import tkinter as tk
from tkinter import filedialog
import os


root = tk.Tk()  # this holds the whole app/ struture
apps = []

if os.path.isfile('apps.txt'):
    with open('apps.txt', mode='r') as file:
        tempApps = file.read()
        tempApps = tempApps.split(',')  # creates a list with the apps from the text file, separeted by ','
        apps = [x for x in tempApps if x.strip()]  # removes whitespaces between app names
                                                   # 'adds' the apps to the empty list (empty because of restart)


def add_app():
    for widget in frame.winfo_children():
        widget.destroy()  # used to remove the initial entries and only show the updated ones if another entry added

    filename = filedialog.askopenfilename(initialdir='/', title='Select File',
                                          filetypes=(('executables', '*.exe'), ('all files', '*.*')))
    apps.append(filename)

    # show the added app on our GUI
    for app in apps:
        label = tk.Label(frame, text=app, bg='white')
        label.pack()


def run_apps():
    for app in apps:
        os.startfile(app)


def delete_apps():
        apps.clear()


# The Canvas is a rectangular area intended for drawing pictures or other complex layouts
canvas = tk.Canvas(root, height=750, width=750, bg='#263D42')
canvas.pack()

# the thing (frame) inside the canvas
frame = tk.Frame(root, bg='white')
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# button
openFile = tk.Button(root, text='Open File', padx=8, pady=2, fg='white', bg='#263D42', command=add_app)
openFile.pack()

# button
deleteAllApps = tk.Button(root, text='Remove All Apps', padx=6, pady=2, fg='white', bg='#263D42', command=delete_apps)
deleteAllApps.pack()

# button
runApps = tk.Button(root, text='Run Apps', padx=8, pady=2, fg='white', bg='#263D42', command=run_apps)
runApps.pack()

# frame that displays apps previously saved in the text file (if they exist)
for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()


root.mainloop()

# write the current session apps in the text file after exit
with open('apps.txt', mode='w') as file:
    for app in apps:
        file.write(app + ',')

