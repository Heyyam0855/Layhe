import tkinter as tk  # Tkinter kitabxanasını import edir
import tkinter.ttk as ttk # Tkinter-in ttk modulu ilə işləmək üçün import edir
import sqlite3 # SQLite3 verilənlər bazası ilə işləmək üçün import edir
from tkinter import font # Tkinter-in font modulu ilə işləmək üçün import edir

db_elage=sqlite3.connect("data.db") # data.db bazasi ile elage yaradacaq
cursor=db_elage.cursor() 
cursor.execute("""CREATE TABLE IF NOT EXISTS users( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    soyad TEXT NOT NULL
)""") 
def update_table():
    # Clear the Treeview
    for row in tree.get_children():
        tree.delete(row)

    # Fetch data from the database
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Insert data into the Treeview
    for row in rows:
        tree.insert("", tk.END, values=row)

def submit():
    ad = name_entry.get()
    soyad = surname_entry.get()
    cursor.execute("INSERT INTO users (ad, soyad) VALUES (?, ?)", (ad, soyad))
    db_elage.commit()
    name_entry.delete(0, tk.END)
    surname_entry.delete(0, tk.END)
    update_table()

def delete_selected():
    selected_item = tree.selection()
    if selected_item:
        for item in selected_item:
            item_values = tree.item(item, 'values')
            cursor.execute("DELETE FROM users WHERE id = ?", (item_values[0],))
            db_elage.commit()
            tree.delete(item)

# Create the main window
app = tk.Tk()
app.title("User Management")
app.geometry("600x400")

# Apply modern styling
app.configure(bg="#f4f4f4")

# Define a modern font
modern_font = font.Font(family="Helvetica", size=12)

# Create and place labels and entry fields
form_frame = tk.Frame(app)
form_frame.pack(pady=10)

name_label = tk.Label(form_frame, text="Ad:", font=modern_font, bg="#f4f4f4")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(form_frame, font=modern_font, relief="solid", bd=1)
name_entry.grid(row=0, column=1, padx=10, pady=5)

surname_label = tk.Label(form_frame, text="Soyad:", font=modern_font, bg="#f4f4f4")
surname_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
surname_entry = tk.Entry(form_frame, font=modern_font, relief="solid", bd=1)
surname_entry.grid(row=1, column=1, padx=10, pady=5)

submit_button = tk.Button(form_frame, text="Təsdiq et", font=modern_font, bg="#0078D7", fg="white", relief="flat", command=submit)
submit_button.grid(row=2, column=0, pady=10, sticky="e")
delete_button = tk.Button(form_frame, text="Sil", font=modern_font, bg="#FF4C4C", fg="white", relief="flat", command=delete_selected)
delete_button.grid(row=2, column=1, pady=10, sticky="w")

# Create a Treeview widget for the table
table_frame = tk.Frame(app)
table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

tree = ttk.Treeview(table_frame, columns=("ID", "Ad", "Soyad"), show="headings", style="Custom.Treeview")
tree.heading("ID", text="ID")
tree.heading("Ad", text="Ad")
tree.heading("Soyad", text="Soyad")

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Add Treeview style
style = ttk.Style()
style.configure("Custom.Treeview", font=("Helvetica", 10), rowheight=25, fieldbackground="#ffffff", background="#ffffff")
style.configure("Custom.Treeview.Heading", font=("Helvetica", 12, "bold"), background="#0078D7", foreground="white")
style.map("Custom.Treeview", background=[("selected", "#0078D7")], foreground=[("selected", "white")])

# Populate the table with initial data
update_table()

# Run the application
if __name__ == "__main__":
    app.mainloop()