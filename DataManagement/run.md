# Tkinter kitabxanasını import edir
import tkinter as tk
# Tkinter-in ttk modulu ilə işləmək üçün import edir
import tkinter.ttk as ttk
# SQLite3 verilənlər bazası ilə işləmək üçün import edir
import sqlite3
# Tkinter-in font modulu ilə işləmək üçün import edir
from tkinter import font

# Verilənlər bazası ilə əlaqə yaradır və cədvəl yaradır
db_elage = sqlite3.connect("data.db")  # data.db bazası ilə əlaqə
cursor = db_elage.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (  # Əgər mövcud deyilsə, 'users' cədvəli yaradır
        id INTEGER PRIMARY KEY AUTOINCREMENT,  # Avtomatik artan ID sütunu
        ad TEXT NOT NULL,  # Boş olmayan ad sütunu
        soyad TEXT NOT NULL  # Boş olmayan soyad sütunu
    )
""")

# Treeview-i verilənlər bazasından alınan məlumatlarla yeniləyən funksiya
def update_table():
    # Treeview-i təmizləyir
    for row in tree.get_children():
        tree.delete(row)

    # Verilənlər bazasından məlumatları alır
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Treeview-ə məlumatları əlavə edir
    for row in rows:
        tree.insert("", tk.END, values=row)

# Yeni istifadəçi əlavə edən funksiya
def submit():
    ad = name_entry.get()  # Adı giriş sahəsindən alır
    soyad = surname_entry.get()  # Soyadı giriş sahəsindən alır
    cursor.execute("INSERT INTO users (ad, soyad) VALUES (?, ?)", (ad, soyad))  # Məlumatı bazaya əlavə edir
    db_elage.commit()  # Dəyişiklikləri saxlayır
    name_entry.delete(0, tk.END)  # Ad sahəsini təmizləyir
    surname_entry.delete(0, tk.END)  # Soyad sahəsini təmizləyir
    update_table()  # Cədvəli yeniləyir

# Seçilmiş istifadəçiləri silən funksiya
def delete_selected():
    selected_item = tree.selection()  # Seçilmiş elementləri alır
    if selected_item:
        for item in selected_item:
            item_values = tree.item(item, 'values')  # Seçilmiş elementin dəyərlərini alır
            cursor.execute("DELETE FROM users WHERE id = ?", (item_values[0],))  # Məlumatı bazadan silir
            db_elage.commit()  # Dəyişiklikləri saxlayır
            tree.delete(item)  # Elementi Treeview-dən silir

# Əsas pəncərəni yaradır
app = tk.Tk()
app.title("User Management")  # Pəncərənin başlığını təyin edir
app.geometry("600x400")  # Pəncərənin ölçüsünü təyin edir
app.configure(bg="#f4f4f4")  # Pəncərənin fon rəngini təyin edir

# Müasir şrift təyin edir
modern_font = font.Font(family="Helvetica", size=12)

# Giriş sahələri və düymələr üçün çərçivə yaradır
form_frame = tk.Frame(app)
form_frame.pack(pady=10)

# Ad etiketi və giriş sahəsi
name_label = tk.Label(form_frame, text="Ad:", font=modern_font, bg="#f4f4f4")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = tk.Entry(form_frame, font=modern_font, relief="solid", bd=1)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Soyad etiketi və giriş sahəsi
surname_label = tk.Label(form_frame, text="Soyad:", font=modern_font, bg="#f4f4f4")
surname_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
surname_entry = tk.Entry(form_frame, font=modern_font, relief="solid", bd=1)
surname_entry.grid(row=1, column=1, padx=10, pady=5)

# Təsdiq və sil düymələri
submit_button = tk.Button(
    form_frame, text="Təsdiq et", font=modern_font, bg="#0078D7", fg="white",
    relief="flat", command=submit
)
submit_button.grid(row=2, column=0, pady=10, sticky="e")

delete_button = tk.Button(
    form_frame, text="Sil", font=modern_font, bg="#FF4C4C", fg="white",
    relief="flat", command=delete_selected
)
delete_button.grid(row=2, column=1, pady=10, sticky="w")

# Treeview üçün çərçivə yaradır
table_frame = tk.Frame(app)
table_frame.pack(fill=tk.BOTH, expand=True, pady=10)

# Treeview widget-ı yaradır
tree = ttk.Treeview(table_frame, columns=("ID", "Ad", "Soyad"), show="headings", style="Custom.Treeview")
tree.heading("ID", text="ID")  # ID sütun başlığı
tree.heading("Ad", text="Ad")  # Ad sütun başlığı
tree.heading("Soyad", text="Soyad")  # Soyad sütun başlığı
tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Treeview üçün stil əlavə edir
style = ttk.Style()
style.configure("Custom.Treeview", font=("Helvetica", 10), rowheight=25, fieldbackground="#ffffff", background="#ffffff")
style.configure("Custom.Treeview.Heading", font=("Helvetica", 12, "bold"), background="#0078D7", foreground="white")
style.map("Custom.Treeview", background=[("selected", "#0078D7")], foreground=[("selected", "white")])

# Cədvəli ilkin məlumatlarla doldurur
update_table()

# Tətbiqi işə salır
if