import customtkinter as ctk
import threading
import time
import math
import socket
import urllib.request
import json
import sqlite3
import random

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Zero XLSX - Spreadsheet Editor")
        self.geometry("800x600")
        self.configure(fg_color="#1a1a24")
        
        # Header
        self.header = ctk.CTkLabel(self, text="Zero XLSX - Spreadsheet Editor", font=("Helvetica", 24, "bold"), text_color="#00C7FF")
        self.header.pack(pady=20)
        
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(fill=ctk.BOTH, expand=True, padx=20, pady=10)
        
        self.setup_ui()
        
    
    def setup_ui(self):
        self.cells = {}
        grid = ctk.CTkFrame(self.main_frame)
        grid.pack(fill=ctk.BOTH, expand=True)
        
        for r in range(10):
            grid.rowconfigure(r, weight=1)
            for c in range(6):
                grid.columnconfigure(c, weight=1)
                entry = ctk.CTkEntry(grid, justify="center")
                entry.grid(row=r, column=c, sticky="nsew", padx=1, pady=1)
                self.cells[(r, c)] = entry
                
        btn = ctk.CTkButton(self.main_frame, text="Calculate Sums (Col 0)", command=self.calc)
        btn.pack(pady=10)
        
    def calc(self):
        total = 0
        for r in range(9):
            val = self.cells[(r, 0)].get()
            if val.isdigit(): total += int(val)
        self.cells[(9, 0)].delete(0, "end")
        self.cells[(9, 0)].insert(0, str(total))


if __name__ == "__main__":
    app = App()
    app.mainloop()
