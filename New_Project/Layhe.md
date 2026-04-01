# Python Tkinter Proqram Pillanı

## 1. Layihə Haqqında

Bu layihə Python proqramlaşdırma dili və onun Tkinter kitabxanasından istifadə edərək qrafik interfeys tətbiqinin yaradılmasını əhatə edir.

## 2. Tələblər

- Python 3.x versiyası
- Tkinter kitabxanası (Python standart kitabxanasına daxildir)
- Əlavə kitabxanalar (tətbiqin ehtiyaclarına görə)

## 3. Qurulum Mərhələləri

1. Python-un yüklənməsi:
   - [python.org](https://www.python.org/downloads/) saytından Python-un son versiyasını yükləyin
   - Quraşdırma zamanı "Add Python to PATH" seçimini işarələyin

2. Tkinter-in yoxlanması:
   ```bash
   python -c "import tkinter; print('Tkinter yükləndi!')"
   ```

3. Layihə qovluğunun yaradılması:
   ```bash
   mkdir tkinter_layihe
   cd tkinter_layihe
   ```

4. Virtual mühitin yaradılması (tövsiyə olunur):
   ```bash
   python -m venv venv
   # Windows üçün
   venv\Scripts\activate
   # Linux/Mac üçün
   # source venv/bin/activate
   ```

## 4. Layihə Strukturu

```
tkinter_layihe/
├── app.py              # Əsas proqram faylı
├── modules/            # Modullar qovluğu
│   ├── __init__.py
│   ├── ui_elements.py  # UI elementləri
│   └── utils.py        # Köməkçi funksiyalar
├── assets/             # Şəkillər və digər resurslar
├── config.ini          # Konfiqurasiya faylı
└── README.md           # Layihə haqqında məlumat
```

## 5. Tətbiq İnkişaf Mərhələləri

### 5.1. Əsas Pəncərənin Yaradılması
```python
import tkinter as tk

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter Tətbiqi")
        self.geometry("800x600")
        self.configure(bg="#f0f0f0")
        
        # Əsas elementlərin əlavə edilməsi
        self.create_widgets()
    
    def create_widgets(self):
        # Nümunə elementlər
        label = tk.Label(self, text="Xoş gəlmisiniz!", font=("Arial", 24))
        label.pack(pady=20)
        
        button = tk.Button(self, text="Klikləyin", command=self.on_button_click)
        button.pack(pady=10)
    
    def on_button_click(self):
        print("Düymə klikləndi!")

if __name__ == "__main__":
    app = Application()
    app.mainloop()
```

### 5.2. Müxtəlif Tkinter Widget-lərin İstifadəsi

- Label (mətn göstərmək üçün)
- Button (düymələr)
- Entry (mətn daxiletmə sahəsi)
- Text (çoxsətirli mətn sahəsi)
- Frame (konteyner)
- Canvas (qrafik çəkmək üçün)
- Listbox (siyahılar)
- Radiobutton və Checkbutton (seçim elementləri)
- Menu (menyu yaratmaq üçün)
- Messagebox (dialoq pəncərələri)

### 5.3. Layout Menecerləri

- pack(): Sadə düzülüş üçün
- grid(): Cədvəl şəklində düzülüş üçün
- place(): Dəqiq koordinatlarla yerləşdirmə üçün

## 6. Nümunə Tətbiqlər

### 6.1. Hesablayıcı (Kalkulyator)
```python
import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hesablayıcı")
        self.geometry("300x400")
        
        self.result_var = tk.StringVar()
        
        # UI yaratma
        self.create_ui()
    
    def create_ui(self):
        # Nəticə sahəsi
        result = tk.Entry(self, textvariable=self.result_var, font=("Arial", 24), justify="right")
        result.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Düymələr
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row, col = 1, 0
        for button in buttons:
            tk.Button(self, text=button, font=("Arial", 18), 
                     command=lambda b=button: self.on_button_click(b)).grid(
                     row=row, column=col, sticky="nsew", padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear düyməsi
        tk.Button(self, text="C", font=("Arial", 18), 
                 command=self.clear).grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
                
        # Sətir və sütunların genişlənməsi
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
    
    def on_button_click(self, button):
        current = self.result_var.get()
        
        if button == "=":
            try:
                result = eval(current)
                self.result_var.set(result)
            except:
                self.result_var.set("Xəta")
        else:
            self.result_var.set(current + button)
    
    def clear(self):
        self.result_var.set("")

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
```

### 6.2. Məlumat Forması
```python
import tkinter as tk
from tkinter import messagebox

class DataForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Məlumat Forması")
        self.geometry("400x300")
        self.create_form()
    
    def create_form(self):
        # Ad sahəsi
        tk.Label(self, text="Ad:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        # Soyad sahəsi
        tk.Label(self, text="Soyad:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        self.surname_entry = tk.Entry(self)
        self.surname_entry.grid(row=1, column=1, padx=10, pady=5)
        
        # Email sahəsi
        tk.Label(self, text="Email:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        # Təqdim et düyməsi
        submit_button = tk.Button(self, text="Təqdim et", command=self.submit_form)
        submit_button.grid(row=3, column=0, columnspan=2, pady=20)
    
    def submit_form(self):
        name = self.name_entry.get()
        surname = self.surname_entry.get()
        email = self.email_entry.get()
        
        if name and surname and email:
            messagebox.showinfo("Uğurlu", f"Məlumatlar qeydə alındı!\nAd: {name}\nSoyad: {surname}\nEmail: {email}")
        else:
            messagebox.showerror("Xəta", "Bütün sahələri doldurun!")

if __name__ == "__main__":
    app = DataForm()
    app.mainloop()
```

## 7. Əlavə Təkmilləşdirmələr

1. Tema və Stillər
   - ttk modulundan istifadə edərək müasir görünüş əlavə etmək
   
2. Məlumat Bazası İnteqrasiyası
   - SQLite, MySQL və ya başqa DB ilə işləmək
   
3. Fayl Əməliyyatları
   - Məlumatları fayla yükləmək və oxumaq
   
4. Çoxdilli Dəstək
   - Müxtəlif dillərdə interfeys təmin etmək

5. İnternetə Qoşulma
   - API-lərlə inteqrasiya və məlumat mübadiləsi

## 8. Layihəni Paylaşmaq

1. Exe faylı yaratmaq (PyInstaller ilə):
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --windowed app.py
   ```

2. Git ilə kodun idarə edilməsi:
   ```bash
   git init
   git add .
   git commit -m "İlk versiya"
   ```

3. GitHub və ya digər kod paylaşım platformalarında yerləşdirmək

## 9. Faydalı Resurslar

- [Python Rəsmi Saytı](https://www.python.org)
- [Tkinter Sənədləri](https://docs.python.org/3/library/tkinter.html)
- [Tkinter Öyrənmək üçün Resurslar](https://realpython.com/python-gui-tkinter/)
- [StackOverflow](https://stackoverflow.com/questions/tagged/tkinter)