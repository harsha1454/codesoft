import tkinter as tk
from tkinter import messagebox
import os

# Function to save tasks to a text file
def save_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        update_task_file()
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to update the task file
def update_task_file():
    with open("tasks.txt", "w") as file:
        for task in tasks_listbox.get(0, tk.END):
            file.write(task + "\n")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
        update_task_file()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to delete all tasks
def delete_all_tasks():
    if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete all tasks?"):
        tasks_listbox.delete(0, tk.END)
        update_task_file()

# Function to mark a task as completed
def mark_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, task + " - Completed")
        update_task_file()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to load saved tasks from file
def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks_listbox.insert(tk.END, line.strip())

# Function to exit the application
def exit_application():
    root.destroy()

# Set up the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x500")
root.config(bg="#f0f8ff")

# Create the task input and button
frame_top = tk.Frame(root, bg="#f0f8ff")
frame_top.pack(pady=10)

label = tk.Label(frame_top, text="To-Do List", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#4b0082")
label.pack()

task_entry = tk.Entry(frame_top, width=35, font=("Helvetica", 12))
task_entry.pack(pady=5)

add_button = tk.Button(frame_top, text="Add Task", width=20, bg="#4b0082", fg="white", font=("Helvetica", 10), command=save_task)
add_button.pack(pady=5)

# Create a listbox to display tasks
frame_middle = tk.Frame(root, bg="#f0f8ff")
frame_middle.pack()

tasks_listbox = tk.Listbox(frame_middle, height=15, width=35, selectmode=tk.SINGLE, font=("Helvetica", 12), bg="#f8f8ff")
tasks_listbox.pack(pady=10)

# Create buttons for task actions
frame_bottom = tk.Frame(root, bg="#f0f8ff")
frame_bottom.pack(pady=10)

delete_button = tk.Button(frame_bottom, text="Delete Task", width=20, bg="#dc143c", fg="white", font=("Helvetica", 10), command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(frame_bottom, text="Mark as Completed", width=20, bg="#228b22", fg="white", font=("Helvetica", 10), command=mark_completed)
mark_button.pack(pady=5)

delete_all_button = tk.Button(frame_bottom, text="Delete All Tasks", width=20, bg="#ff8c00", fg="white", font=("Helvetica", 10), command=delete_all_tasks)
delete_all_button.pack(pady=5)

exit_button = tk.Button(frame_bottom, text="Exit", width=20, bg="#4682b4", fg="white", font=("Helvetica", 10), command=exit_application)
exit_button.pack(pady=5)

# Load existing tasks
load_tasks()

# Start the GUI
root.mainloop()
