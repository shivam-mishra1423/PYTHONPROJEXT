import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('hospital_management.db')
cursor = conn.cursor()

# Create the prescriptions table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS prescriptions (
                    tablet_name TEXT,
                    reference_no TEXT,
                    dose INTEGER,
                    no_of_tablets INTEGER,
                    lot TEXT,
                    issue_date TEXT,
                    exp_date TEXT,
                    daily_dose INTEGER,
                    side_effect TEXT,
                    further_info TEXT,
                    blood_pressure INTEGER,
                    storage_advice TEXT,
                    medication TEXT,
                    patient_id TEXT,
                    nhs_number TEXT,
                    patient_name TEXT,
                    dob TEXT,
                    address TEXT
                )''')
conn.commit()

# Functions
def add_prescription():
    cursor.execute('''INSERT INTO prescriptions VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (tablet_name_entry.get(), reference_no_entry.get(), dose_entry.get(), no_of_tablets_entry.get(),
                    lot_entry.get(), issue_date_entry.get(), exp_date_entry.get(), daily_dose_entry.get(),
                    side_effect_entry.get(), further_info_entry.get(), blood_pressure_entry.get(),
                    storage_advice_entry.get(), medication_entry.get(), patient_id_entry.get(),
                    nhs_number_entry.get(), patient_name_entry.get(), dob_entry.get(), address_entry.get()))
    conn.commit()
    messagebox.showinfo("Success", "Prescription added successfully")
    reset_fields()
    load_data()

def update_prescription():
    cursor.execute('''UPDATE prescriptions SET
                        dose=?, no_of_tablets=?, lot=?, issue_date=?, exp_date=?, daily_dose=?, side_effect=?,
                        further_info=?, blood_pressure=?, storage_advice=?, medication=?, nhs_number=?, patient_name=?,
                        dob=?, address=? WHERE tablet_name=? AND reference_no=? AND patient_id=?''',
                   (dose_entry.get(), no_of_tablets_entry.get(), lot_entry.get(), issue_date_entry.get(),
                    exp_date_entry.get(), daily_dose_entry.get(), side_effect_entry.get(), further_info_entry.get(),
                    blood_pressure_entry.get(), storage_advice_entry.get(), medication_entry.get(),
                    nhs_number_entry.get(), patient_name_entry.get(), dob_entry.get(), address_entry.get(),
                    tablet_name_entry.get(), reference_no_entry.get(), patient_id_entry.get()))
    conn.commit()
    messagebox.showinfo("Success", "Prescription updated successfully")
    load_data()

def delete_prescription():
    cursor.execute('''DELETE FROM prescriptions WHERE tablet_name=? AND reference_no=? AND patient_id=?''',
                   (tablet_name_entry.get(), reference_no_entry.get(), patient_id_entry.get()))
    conn.commit()
    messagebox.showinfo("Success", "Prescription deleted successfully")
    reset_fields()
    load_data()

def reset_fields():
    for entry in entries.values():
        entry.delete(0, tk.END)

def load_data():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM prescriptions")
    records = cursor.fetchall()
    for record in records:
        tree.insert("", tk.END, values=record)

def exit_app():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Hospital Management System")
root.geometry("1200x700")
root.configure(bg="white")

# Title
title_label = tk.Label(root, text="HOSPITAL MANAGEMENT SYSTEM", font=("Arial", 24, "bold"), fg="red")
title_label.pack(pady=10)

# Frame for Patient Information Form
form_frame = tk.Frame(root, bg="white", padx=10, pady=10)
form_frame.pack(pady=10, fill="x")

# Fields in the form
fields = [
    ("Name Of Tablets", 0, 0), ("Reference No", 1, 0), ("Dose", 2, 0), ("No Of Tablets", 3, 0),
    ("Lot", 4, 0), ("Issue Date", 5, 0), ("Exp Date", 6, 0), ("Daily Dose", 7, 0),
    ("Side Effect", 8, 0), ("Further Information", 0, 2), ("Blood Pressure", 1, 2),
    ("Storage Advice", 2, 2), ("Medication", 3, 2), ("Patient Id", 4, 2),
    ("NHS Number", 5, 2), ("Patient Name", 6, 2), ("Date Of Birth", 7, 2), ("Patient Address", 8, 2)
]

entries = {}
for label_text, row, col in fields:
    label = tk.Label(form_frame, text=label_text, bg="white", font=("Arial", 10, "bold"))
    label.grid(row=row, column=col, padx=10, pady=5, sticky="e")
    entry = tk.Entry(form_frame, width=30)
    entry.grid(row=row, column=col + 1, padx=10, pady=5)
    entries[label_text.replace(" ", "_").lower()] = entry

# Map entries to variables for easier access
tablet_name_entry = entries["name_of_tablets"]
reference_no_entry = entries["reference_no"]
dose_entry = entries["dose"]
no_of_tablets_entry = entries["no_of_tablets"]
lot_entry = entries["lot"]
issue_date_entry = entries["issue_date"]
exp_date_entry = entries["exp_date"]
daily_dose_entry = entries["daily_dose"]
side_effect_entry = entries["side_effect"]
further_info_entry = entries["further_information"]
blood_pressure_entry = entries["blood_pressure"]
storage_advice_entry = entries["storage_advice"]
medication_entry = entries["medication"]
patient_id_entry = entries["patient_id"]
nhs_number_entry = entries["nhs_number"]
patient_name_entry = entries["patient_name"]
dob_entry = entries["date_of_birth"]
address_entry = entries["patient_address"]

# Buttons for actions
button_frame = tk.Frame(root, bg="white", pady=10)
button_frame.pack(fill="x")
button_texts = [("Add", add_prescription), ("Update", update_prescription), ("Delete", delete_prescription),
                ("Reset", reset_fields), ("Exit", exit_app)]
for i, (text, command) in enumerate(button_texts):
    button = tk.Button(button_frame, text=text, command=command, width=15, bg="green", fg="white", font=("Arial", 10, "bold"))
    button.grid(row=0, column=i, padx=5, pady=5)

# Table to display prescriptions
table_frame = tk.Frame(root, bg="white")
table_frame.pack(pady=10, fill="both", expand=True)

columns = ["tablet_name", "reference_no", "dose", "no_of_tablets", "lot", "issue_date", "exp_date", "daily_dose",
           "side_effect", "further_info", "blood_pressure", "storage_advice", "medication", "patient_id",
           "nhs_number", "patient_name", "dob", "address"]

tree = ttk.Treeview(table_frame, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col.replace("_", " ").title())
    tree.column(col, width=100)
tree.pack(side="left", fill="both", expand=True)

# Add a scrollbar to the table
scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.config(yscrollcommand=scrollbar.set)

load_data()
root.mainloop()
