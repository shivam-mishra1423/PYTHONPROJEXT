from tkinter import *
from tkinter import ttk, messagebox

# Main window setup
root = Tk()
root.title("Library Management System")
root.geometry("1200x600")

# Variables
member_type = StringVar()
prn_no = StringVar()
id_no = StringVar()
first_name = StringVar()
surname = StringVar()
address1 = StringVar()
address2 = StringVar()
post_code = StringVar()
mobile_no = StringVar()
book_id = StringVar()
book_title = StringVar()
author_name = StringVar()
date_borrowed = StringVar()
date_due = StringVar()
days_on_book = StringVar()
late_return_fine = StringVar()
date_over_due = StringVar()
actual_price = StringVar()

# Frame for Library Membership Information
frame1 = LabelFrame(root, text="Library Membership Information", font=("Arial", 12, "bold"), padx=10, pady=10)
frame1.place(x=20, y=70, width=550, height=400)

# Labels and Entry widgets for frame1
Label(frame1, text="Member Type").grid(row=0, column=0, sticky=W, padx=5, pady=5)
ttk.Combobox(frame1, textvariable=member_type, values=["Admin Staff", "Lecturer", "Student"]).grid(row=0, column=1, padx=5, pady=5)

Label(frame1, text="PRN No").grid(row=1, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=prn_no).grid(row=1, column=1, padx=5, pady=5)

Label(frame1, text="ID No").grid(row=2, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=id_no).grid(row=2, column=1, padx=5, pady=5)

Label(frame1, text="First Name").grid(row=3, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=first_name).grid(row=3, column=1, padx=5, pady=5)

Label(frame1, text="Surname").grid(row=4, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=surname).grid(row=4, column=1, padx=5, pady=5)

Label(frame1, text="Address1").grid(row=5, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=address1).grid(row=5, column=1, padx=5, pady=5)

Label(frame1, text="Address2").grid(row=6, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=address2).grid(row=6, column=1, padx=5, pady=5)

Label(frame1, text="Post Code").grid(row=7, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=post_code).grid(row=7, column=1, padx=5, pady=5)

Label(frame1, text="Mobile Number").grid(row=8, column=0, sticky=W, padx=5, pady=5)
Entry(frame1, textvariable=mobile_no).grid(row=8, column=1, padx=5, pady=5)

# Function to reset fields
def reset_fields():
    member_type.set("")
    prn_no.set("")
    id_no.set("")
    first_name.set("")
    surname.set("")
    address1.set("")
    address2.set("")
    post_code.set("")
    mobile_no.set("")
    book_id.set("")
    book_title.set("")
    author_name.set("")
    date_borrowed.set("")
    date_due.set("")
    days_on_book.set("")
    late_return_fine.set("")
    date_over_due.set("")
    actual_price.set("")

# Frame to display data
frame_data = Frame(root)
frame_data.place(x=20, y=450, width=1150, height=200)

# Treeview for data display
tree = ttk.Treeview(frame_data, columns=("member_type", "prn_no", "id_no", "first_name", "surname", "address1", "address2", "post_code", "mobile_no"), show="headings")
tree.heading("member_type", text="Member Type")
tree.heading("prn_no", text="PRN No")
tree.heading("id_no", text="ID No")
tree.heading("first_name", text="First Name")
tree.heading("surname", text="Surname")
tree.heading("address1", text="Address1")
tree.heading("address2", text="Address2")
tree.heading("post_code", text="Post Code")
tree.heading("mobile_no", text="Mobile Number")
tree.pack(fill=BOTH, expand=True)

# Example data for Treeview
def show_data():
    # Clearing existing data
    for i in tree.get_children():
        tree.delete(i)
    
    # Adding example data
    example_data = [
        (member_type.get(), prn_no.get(), id_no.get(), first_name.get(), surname.get(), address1.get(), address2.get(), post_code.get(), mobile_no.get())
    ]
    
    for row in example_data:
        tree.insert("", END, values=row)

# Buttons for actions
frame3 = Frame(root)
frame3.place(x=20, y=500, width=1100, height=50)

Button(frame3, text="Add Data", width=15, command=lambda: messagebox.showinfo("Action", "Data added")).grid(row=0, column=0, padx=10, pady=10)
Button(frame3, text="Show Data", width=15, command=show_data).grid(row=0, column=1, padx=10, pady=10)
Button(frame3, text="Update", width=15, command=lambda: messagebox.showinfo("Action", "Data updated")).grid(row=0, column=2, padx=10, pady=10)
Button(frame3, text="Delete", width=15, command=lambda: messagebox.showinfo("Action", "Data deleted")).grid(row=0, column=3, padx=10, pady=10)
Button(frame3, text="Reset", width=15, command=reset_fields).grid(row=0, column=4, padx=10, pady=10)
Button(frame3, text="Exit", width=15, command=root.quit).grid(row=0, column=5, padx=10, pady=10)

# Run the application
root.mainloop()
