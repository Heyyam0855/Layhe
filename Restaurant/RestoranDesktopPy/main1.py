import tkinter as tk
from tkinter import messagebox


class RestoranProgrami:
    def __init__(self,adi,genislik,hundurluk):
        self.program=tk.Tk()
        self.program.title(adi)
        self.program.geometry(f"{genislik}x{hundurluk}")
        self.program.mainloop()


restoran=RestoranProgrami("Yeni Program",400,500)