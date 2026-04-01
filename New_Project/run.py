import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class QeydiyyatFormasi(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Qeydiyyat Forması")
        self.geometry("500x400")
        self.configure(bg="#f0f0f0")
        self.create_widgets()
        
    def create_widgets(self):
        # Ana çərçivə
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Başlıq
        title_label = ttk.Label(main_frame, text="İstifadəçi Qeydiyyatı", 
                            font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Ad sahəsi
        ttk.Label(main_frame, text="Ad:").grid(row=1, column=0, 
                                          sticky=tk.W, pady=5)
        self.ad_entry = ttk.Entry(main_frame, width=30)
        self.ad_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # Soyad sahəsi
        ttk.Label(main_frame, text="Soyad:").grid(row=2, column=0, 
                                             sticky=tk.W, pady=5)
        self.soyad_entry = ttk.Entry(main_frame, width=30)
        self.soyad_entry.grid(row=2, column=1, pady=5, padx=5)
        
        # Email sahəsi
        ttk.Label(main_frame, text="Email:").grid(row=3, column=0, 
                                             sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(main_frame, width=30)
        self.email_entry.grid(row=3, column=1, pady=5, padx=5)
        
        # Şifrə sahəsi
        ttk.Label(main_frame, text="Şifrə:").grid(row=4, column=0, 
                                             sticky=tk.W, pady=5)
        self.sifre_entry = ttk.Entry(main_frame, width=30, show="*")
        self.sifre_entry.grid(row=4, column=1, pady=5, padx=5)
        
        # Şifrəni təkrarlayın
        ttk.Label(main_frame, text="Şifrəni təkrarlayın:").grid(row=5, column=0, 
                                                           sticky=tk.W, pady=5)
        self.sifre_tekrar_entry = ttk.Entry(main_frame, width=30, show="*")
        self.sifre_tekrar_entry.grid(row=5, column=1, pady=5, padx=5)
        
        # Cinsiyyət seçimi
        ttk.Label(main_frame, text="Cinsiyyət:").grid(row=6, column=0, 
                                                sticky=tk.W, pady=5)
        self.cinsiyyet = tk.StringVar()
        self.cinsiyyet.set("Kişi")
        ttk.Radiobutton(main_frame, text="Kişi", variable=self.cinsiyyet,
                    value="Kişi").grid(row=6, column=1, sticky=tk.W, pady=5)
        ttk.Radiobutton(main_frame, text="Qadın", variable=self.cinsiyyet,
                    value="Qadın").grid(row=6, column=1, pady=5, padx=(50, 0))
        
        # Yaş seçimi
        ttk.Label(main_frame, text="Yaş:").grid(row=7, column=0, 
                                           sticky=tk.W, pady=5)
        self.yas = tk.StringVar()
        age_values = [str(i) for i in range(18, 81)]
        age_combobox = ttk.Combobox(main_frame, textvariable=self.yas, 
                                values=age_values, width=5)
        age_combobox.grid(row=7, column=1, sticky=tk.W, pady=5)
        age_combobox.set("18")
        
        # Şərtləri qəbul et
        self.accept_var = tk.BooleanVar()
        ttk.Checkbutton(main_frame, text="İstifadəçi şərtlərini qəbul edirəm", 
                    variable=self.accept_var).grid(row=8, column=0,
                    columnspan=2, sticky=tk.W, pady=10)
        
        # Düymələr çərçivəsi
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.grid(row=9, column=0, columnspan=2, pady=10)
        
        # Qeydiyyat düyməsi
        qeydiyyat_button = ttk.Button(buttons_frame, text="Qeydiyyatdan keç",
                                  command=self.qeydiyyat)
        qeydiyyat_button.pack(side=tk.LEFT, padx=5)
        
        # Təmizlə düyməsi
        temizle_button = ttk.Button(buttons_frame, text="Təmizlə",
                               command=self.temizle)
        temizle_button.pack(side=tk.LEFT, padx=5)
    
    def qeydiyyat(self):
        # Məlumatları almaq
        ad = self.ad_entry.get()
        soyad = self.soyad_entry.get()
        email = self.email_entry.get()
        sifre = self.sifre_entry.get()
        sifre_tekrar = self.sifre_tekrar_entry.get()
        cinsiyyet = self.cinsiyyet.get()
        yas = self.yas.get()
        accept = self.accept_var.get()
        
        # Sahələrin yoxlanması
        if not all([ad, soyad, email, sifre, sifre_tekrar, yas]):
            messagebox.showerror("Xəta", "Bütün sahələri doldurun!")
            return
        
        if sifre != sifre_tekrar:
            messagebox.showerror("Xəta", "Şifrələr eyni deyil!")
            return
        
        if not accept:
            messagebox.showerror("Xəta", "İstifadəçi şərtlərini qəbul edin!")
            return
            
        # Uğurlu qeydiyyat
        messagebox.showinfo("Uğurlu", f"{ad} {soyad}, qeydiyyat uğurla tamamlandı!")
        
    def temizle(self):
        # Bütün sahələri təmizləmək
        self.ad_entry.delete(0, tk.END)
        self.soyad_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.sifre_entry.delete(0, tk.END)
        self.sifre_tekrar_entry.delete(0, tk.END)
        self.cinsiyyet.set("Kişi")
        self.yas.set("18")
        self.accept_var.set(False)

# Proqramı başlatmaq
if __name__ == "__main__":
    app = QeydiyyatFormasi()
    app.mainloop()
