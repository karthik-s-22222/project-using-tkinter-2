import os
import sys
import tkinter as tr
from tkinter import *                        # This is working for scroll function for my Task pad
from tkinter.messagebox import showinfo      # T0his is working for message box in help_menu to show my typed info
from tkinter import TkVersion 
from tkinter import filedialog, messagebox, simpledialog
from datetime import datetime


# --- TASK PAD (TEXT EDITOR) ---
def open_think_pad():
    simple = tr.Tk()                    
    simple.title (" Think Pad (TP) ")
    simple.geometry( '900x600' )

    # Font setter/setting
    text =tr.Text(
        simple,
        simple.title(" Untilted - Think Pad "),
        wrap=tr.WORD,
        font=('Times New Roman', 14)
    )

    text.pack(expand=True,fill=tr.BOTH)

    #new, open, save, exit
    def new_tasks():
        simple.title( " Untitled - Think Pad " )
        think = None
        text.delete(1.0, tr.END)

    def open_tasks():
        file_path= filedialog.askopenfilename(
        defaultextension='.txt',
        filetypes = [("All Files ","*.*"),(" Think Files ", '*.txt' ,)]
    )

        if file_path:
            with open (file_path, 'r') as file:
                    text.delete(1.0,tr.END)
                    text.insert(tr.END, file.read())

    def save_tasks():
        file_path =filedialog.asksaveasfilename(initialfile= 'untitled.txt',
        defaultextension= '.txt',
        filetypes = [("All Files ","*.*"),('Think Files,' ".txt")]
    )
        
        if file_path:
            with open(file_path, 'w') as file:
                file.write(text.get (1.0, tr.END))
                                                                         
                messagebox.showinfo ("Info", ' The Task Was Saved Successfully ') # after saving pop/confirm alert will be displayed
   


    def print_task():
        content = text.get(1.0, tr.END)
        think_file = "print_think_file.txt"
        with open(think_file, "w") as file:
         file.write(content)
        try:
            if os.name == 'nt': 
                os.startfile(think_file, "print")
        
                messagebox.showinfo("Print", "Sent to printer successfully!")
        except Exception as E:
            messagebox.showerror("Error", f"Could not print: {E}")


    def cut():
            text.event_generate(("<<Cut>>"))

    def copy():
            text.event_generate(("<<Copy>>"))

    def paste():
            text.event_generate(("<<Paste>>"))


    #This is for real date and time in my Think pad   
    def date_time():
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
        text.insert('insert', current_time)

    font_size = 14  
    def zoom_in():
        global font_size
        font_size += 4
        text.config(font=('Times New Roman', font_size))
    font_size = 14
    def zoom_out():
        global font_size
        if font_size  > 4: 
            font_size -= 2
            text.config(font=('Times New Roman', font_size))

         #Message
    def help_menu():
        showinfo("Think Pad Message" , '''My Name is 'karthik.S'
    Thank you For Visting Think Pad''')
      
    def version():
        messagebox.showinfo("Version Info", f"python version: {sys.version}\n Tkinter Version: {tr.TkVersion}")

            #Scroll bar command for task pad
    Scroll =Scrollbar(text)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=text.yview)
    text.config(yscrollcommand=Scroll.set)


    Menu = tr.Menu(simple)
    simple.config(menu=Menu)


    ToDoList_menu=tr.Menu(Menu,tearoff=0)
    Edit_menu =tr.Menu(Menu, tearoff=0)
    date_time_menu = tr.Menu(Menu, tearoff=0)
    zoom_menu = tr.Menu(Menu, tearoff=0)
    Help_menu =tr.Menu(Menu, tearoff=0)

    Menu.add_cascade(label='TodoList', menu=ToDoList_menu)
    Menu.add_cascade(label='Edit',menu= Edit_menu)
    Menu.add_cascade(label="Date & Time", menu= date_time_menu)
    Menu.add_cascade(label="Zoom",menu= zoom_menu)
    Menu.add_cascade(label="Help",menu= Help_menu)

    ToDoList_menu.add_command(label="New", command= new_tasks)
    ToDoList_menu.add_command(label='Open', command= open_tasks)
    ToDoList_menu.add_command(label="Save", command= save_tasks)
    ToDoList_menu.add_command(label="print", command= print_task)
    ToDoList_menu.add_separator()
    ToDoList_menu.add_command(label='Exit', command=simple.quit)

    Edit_menu.add_command(label="cut_tasks", command= cut)
    Edit_menu.add_command(label='copy_tasks', command= copy)
    Edit_menu.add_command(label="paste_Tasks", command= paste)

    date_time_menu.add_command(label="Real Date & Time", command= date_time)

    zoom_menu.add_command(label="Zoom In", command= zoom_in)
    zoom_menu.add_command(label="Zoom Out", command= zoom_out)

    Help_menu.add_command(label="Message", command= help_menu)
    Help_menu.add_command(label="version", command= version)


    
# --- TASK MANAGER (LIST VIEW) ---
tasks = []

def open_task_list():
    simple = tr.Tk()
    simple.title("Task Manager - List")
    simple.geometry('400x500')

    label = tr.Label(simple, text="My To-Do List", font=("Arial", 12, "bold"))
    label.pack(pady=10)

    listbox = tr.Listbox(simple, font=("Arial", 12), selectmode=tr.SINGLE)
    listbox.pack(expand=True, fill=tr.BOTH, padx=20, pady=5)

    def load_data():
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as f:
                for line in f:
                    tasks.append(line.strip())
                    listbox.insert(tr.END, line.strip())

    def add_item():
        new = simpledialog.askstring("Add Task", "What needs to be done?")
        if new:
            tasks.append(new)
            listbox.insert(tr.END, new)
            save_data()

    def delete_item():
        try:
            idx = listbox.curselection()[0]
            listbox.delete(idx)
            tasks.pop(idx)
            save_data()
        except:
            messagebox.showwarning("Selection", "Please select a task to delete!")

    def save_data():
        with open("tasks.txt", "w") as f:
            for t in tasks:
                f.write(t + "\n")

    # Buttons for List
    btn_frame = tr.Frame(simple)
    btn_frame.pack(fill=tr.X, pady=10)
    tr.Button(btn_frame, text="+ Add Task", bg="#d1ffd1", command=add_item).pack(side=tr.LEFT, padx=30)
    tr.Button(btn_frame, text="- Delete", bg="#ffd1d1", command=delete_item).pack(side=tr.RIGHT, padx=30)

    load_data()

# --- MAIN DASHBOARD ---
simple = tr.Tk()
simple.title("My Editor - Dashboard")
simple.geometry("400x300")

tr.Label(simple, text="Welcome to My Page", font=("Arial", 16, "bold")).pack(pady=20)

# The Two Separate Buttons
btn_pad = tr.Button(simple, text="📝 Press to Open Think Pad (Editor)", width=30, height=2, 
                    command= open_think_pad, bg="#e1fef0")
btn_pad.pack(pady=10)

btn_list = tr.Button(simple, text="📋 press to Open Task Manager (List)", width=30, height=2, 
                     command=open_task_list, bg="#fff9c4")
btn_list.pack(pady=10)

simple.mainloop()
