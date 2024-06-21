import tkinter as tk
from tkinter import simpledialog as sd
from tkinter import messagebox as mb

students = { }

def add_student():
    name = sd.askstring("Student Name ","Enter Name : ")
    grade = sd.askstring("Student Marks ","Enter Marks :")
    students[name] = grade
    mb.showinfo("Success","Student Added Successfully")

def update_student():
    if not students:
        mb.showwarning("No Students","No Students Available to Update !")

    os = sd.askstring("Update Student","Enter Student Name To be updated : ")
    if os in students:
        u_grade = sd.askstring("Student Marks ","Enter Marks :")
        students[os] = u_grade
        mb.showinfo("Success","Student Marks Updated Successfully")
    else:
        mb.showerror("Student Not Found !")

def delete_student():
    if not students:
        mb.showwarning("No Students","No Students Present To be Deleted !")

    ds = sd.askstring("Delete Student","Enter Student Name To be Deleted :")
    if ds in students:
        del students[ds]
        mb.showinfo("Success !","Deleted Successfully !")
    else:
        mb.showerror("Student Not Found !")

def view_students():
    if not students:
        mb.showwarning("No Students","Nothing To View ! Add Students")
    mb.showinfo("View Students",students)

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Students Grade Management System By OP")


root.configure(bg='black')

title_label = tk.Label(root,text="Welcome To Student Grade Management System", font=("Helvetica", 20, "bold"),fg='cyan',bg='black')
title_label.pack(padx=10,pady=10)

b_c = {
    'fg':'cyan',
    'bg':'black',
    'activeforeground':'cyan'
    ,'activebackground':'black'
    ,'width':25
}

ab = tk.Button(root,text="Add Student",command=add_student)
ab.pack(padx=5,pady=5)

ub = tk.Button(root,text="Update Student",command=update_student)
ub.pack(padx=5,pady=5)

db = tk.Button(root,text="Delete Student",command=delete_student)
db.pack(padx=5,pady=5)

vb = tk.Button(root,text="View Students",command=view_students)
vb.pack(padx=5,pady=5)

eb = tk.Button(root,text="Exit System",command=exit_app)
eb.pack(padx=5,pady=5)

root.mainloop()