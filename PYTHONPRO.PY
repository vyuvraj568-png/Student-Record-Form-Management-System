from tkinter import *
from tkinter import messagebox
import csv
import os

root = Tk()
root.title("Student Record Management System")
root.geometry("500x500")

# File to save records
file_name = "student_records.csv"

# Ensure file exists
if not os.path.exists(file_name):
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Roll No", "Marks"])

# Functions
def add_record():
    name = name_entry.get()
    roll = roll_entry.get()
    marks = marks_entry.get()

    if name == "" or roll == "" or marks == "":
        messagebox.showwarning("Input Error", "Please fill all fields!")
        return

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, roll, marks])

    messagebox.showinfo("Success", "Record added successfully!")
    name_entry.delete(0, END)
    roll_entry.delete(0, END)
    marks_entry.delete(0, END)
    show_records()

def show_records():
    listbox.delete(0, END)
    with open(file_name, "r") as file:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        reader = csv.reader(file)
        next(reader)  # skip header
        for row in reader:
            listbox.insert(END, f"Name: {row[0]} | Roll No: {row[1]} | Marks: {row[2]}")

def search_record():
    roll = roll_entry.get()
    if roll == "":
        messagebox.showwarning("Input Error", "Please enter Roll No to search!")
        return

    found = False
    listbox.delete(0, END)
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == roll:
                listbox.insert(END, f"Found -> Name: {row[0]}, Roll No: {row[1]}, Marks: {row[2]}")
                found = True
                break
    if not found:
        messagebox.showinfo("Not Found", f"No record found with Roll No: {roll}")

def delete_record():
    roll = roll_entry.get()
    if roll == "":
        messagebox.showwarning("Input Error", "Please enter Roll No to delete!")
        return

    rows = []
    found = False

    with open(file_name, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 1 and row[1] != roll:
                rows.append(row)
            elif len(row) > 1 and row[1] == roll:
                found = True

    if found:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        messagebox.showinfo("Deleted", f"Record with Roll No {roll} deleted successfully!")
        show_records()
    else:
        messagebox.showinfo("Not Found", f"No record found with Roll No: {roll}")

# GUI Layout
Label(root, text="STUDENT RECORD MANAGEMENT", font=("Arial", 16, "bold")).pack(pady=10)

frame = Frame(root)
frame.pack(pady=5)

Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(frame, width=30)
name_entry.grid(row=0, column=1)

Label(frame, text="Roll No:").grid(row=1, column=0, padx=5, pady=5)
roll_entry = Entry(frame, width=30)
roll_entry.grid(row=1, column=1)

Label(frame, text="Marks:").grid(row=2, column=0, padx=5, pady=5)
marks_entry = Entry(frame, width=30)
marks_entry.grid(row=2, column=1)

Button(root, text="Add Record", bg="lightgreen", command=add_record).pack(pady=5)
Button(root, text="Show All Records", bg="lightblue", command=show_records).pack(pady=5)
Button(root, text="Search by Roll No", bg="khaki", command=search_record).pack(pady=5)
Button(root, text="Delete by Roll No", bg="tomato", command=delete_record).pack(pady=5)

listbox = Listbox(root, width=60, height=10)
listbox.pack(pady=10)

show_records()  # Show existing records at startup

root.mainloop()
