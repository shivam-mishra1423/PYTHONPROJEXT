from tkinter import *
from tkinter import ttk, messagebox

# Main window setup
root = Tk()
root.title("Student Management and Study Time Table System")
root.geometry("1200x700")

# Variables for Student Information
student_id = StringVar()
first_name = StringVar()
last_name = StringVar()
age = StringVar()
gender = StringVar()
course = StringVar()
mobile_no = StringVar()

# Variables for Time Table Management
subject = StringVar()
day = StringVar()
time = StringVar()
room = StringVar()

# Frame for Student Information
frame1 = LabelFrame(root, text="Student Information", font=("Arial", 12, "bold"), padx=10, pady=10)
frame1.place(x=20, y=70, width=550, height=300)

# Labels and Entry widgets for Student Information
Label(frame1, text="Student ID").grid(row=0, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=student_id).grid(row=0, column=1, padx=5, pady=5)

Label(frame1, text="First Name").grid(row=1, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=first_name).grid(row=1, column=1, padx=5, pady=5)

Label(frame1, text="Last Name").grid(row=2, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=last_name).grid(row=2, column=1, padx=5, pady=5)

Label(frame1, text="Age").grid(row=3, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=age).grid(row=3, column=1, padx=5, pady=5)

Label(frame1, text="Gender").grid(row=4, column=0, sticky=W, padx=5, pady=5)
ttk.Combobox(frame1, textvariable=gender, values=["Male", "Female"]).grid(row=4, column=1, padx=5, pady=5)

Label(frame1, text="Course").grid(row=5, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=course).grid(row=5, column=1, padx=5, pady=5)

Label(frame1, text="Mobile No").grid(row=6, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=mobile_no).grid(row=6, column=1, padx=5, pady=5)

# Frame for Time Table Management
frame2 = LabelFrame(root, text="Study Time Table", font=("Arial", 12, "bold"), padx=10, pady=10)
frame2.place(x=600, y=70, width=550, height=300)

# Labels and Entry widgets for Time Table
Label(frame2, text="Subject").grid(row=0, column=0, sticky=W, padx=5, pady=5)
Entry(frame2, textvariable=subject).grid(row=0, column=1, padx=5, pady=5)

Label(frame2, text="Day").grid(row=1, column=0, sticky=W, padx=5, pady=5)
ttk.Combobox(frame2, textvariable=day, values=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]).grid(row=1, column=1, padx=5, pady=5)

Label(frame2, text="Time").grid(row=2, column=0, sticky=W, padx=5, pady=5)
Entry(frame2, textvariable=time).grid(row=2, column=1, padx=5, pady=5)

Label(frame2, text="Room No").grid(row=3, column=0, sticky=W, padx=5, pady=5)
Entry(frame2, textvariable=room).grid(row=3, column=1, padx=5, pady=5)

# Treeview for displaying Student Information
frame3 = Frame(root)
frame3.place(x=20, y=400, width=550, height=250)

tree_student = ttk.Treeview(frame3, columns=("student_id", "first_name", "last_name", "age", "gender", "course", "mobile_no"), show="headings")
tree_student.heading("student_id", text="Student ID")
tree_student.heading("first_name", text="First Name")
tree_student.heading("last_name", text="Last Name")
tree_student.heading("age", text="Age")
tree_student.heading("gender", text="Gender")
tree_student.heading("course", text="Course")
tree_student.heading("mobile_no", text="Mobile No")
tree_student.pack(fill=BOTH, expand=True)

# Treeview for displaying Study Time Table
frame4 = Frame(root)
frame4.place(x=600, y=400, width=550, height=250)

tree_timetable = ttk.Treeview(frame4, columns=("subject", "day", "time", "room"), show="headings")
tree_timetable.heading("subject", text="Subject")
tree_timetable.heading("day", text="Day")
tree_timetable.heading("time", text="Time")
tree_timetable.heading("room", text="Room No")
tree_timetable.pack(fill=BOTH, expand=True)

# Functions for managing data
def add_student():
    # Adding student data to Treeview
    tree_student.insert("", END, values=(student_id.get(), first_name.get(), last_name.get(), age.get(), gender.get(), course.get(), mobile_no.get()))
    messagebox.showinfo("Success", "Student Added Successfully!")

def add_timetable():
    # Adding timetable data to Treeview
    tree_timetable.insert("", END, values=(subject.get(), day.get(), time.get(), room.get()))
    messagebox.showinfo("Success", "Time Table Added Successfully!")

def reset_fields():
    # Reset all fields
    student_id.set("")
    first_name.set("")
    last_name.set("")
    age.set("")
    gender.set("")
    course.set("")
    mobile_no.set("")
    subject.set("")
    day.set("")
    time.set("")
    room.set("")

# Buttons for Actions
frame5 = Frame(root)
frame5.place(x=20, y=660, width=1150, height=50)

Button(frame5, text="Add Student", width=15, command=add_student).grid(row=0, column=0, padx=10, pady=10)
Button(frame5, text="Add Time Table", width=15, command=add_timetable).grid(row=0, column=1, padx=10, pady=10)
Button(frame5, text="Reset", width=15, command=reset_fields).grid(row=0, column=2, padx=10, pady=10)
Button(frame5, text="Exit", width=15, command=root.quit).grid(row=0, column=3, padx=10, pady=10)

# Run the application
root.mainloop()
