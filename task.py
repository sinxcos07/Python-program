# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 13:14:14 2024

@author: zeb
"""

import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.task_list = []

        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10)
        self.task_listbox.pack(pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(pady=5)

        # Load previously saved tasks on startup
        self.load_tasks()

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.task_list.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.task_list[index]
            self.task_listbox.delete(index)
        else:
            messagebox.showwarning("No Task Selected", "Please select a task to delete.")

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.task_list:
                file.write(task + "\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                tasks = file.read().splitlines()
                self.task_list = tasks
                self.task_listbox.delete(0, tk.END)
                for task in tasks:
                    self.task_listbox.insert(tk.END, task)
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()
