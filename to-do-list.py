import tkinter as tk

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

def remove_task():
    selected_task = listbox_tasks.curselection()
    if selected_task:
        listbox_tasks.delete(selected_task)

root = tk.Tk()
root.title("Список задач")

entry_task = tk.Entry(root, width=30)
entry_task.pack()

button_add = tk.Button(root, text="Добавить задачу", command=add_task)
button_add.pack()

button_remove = tk.Button(root, text="Удалить задачу", command=remove_task)
button_remove.pack()

listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.pack()

root.mainloop()
