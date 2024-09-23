import tkinter as tk
from tela import tela
from database.tables.createTables import create_tables
from database.tables.produtos import select_all

def root():
    root= tk.Tk()
    root.geometry("600x600")
    root.title("Sunshine") 
    create_tables()
    select_all()
    tela(root)
    return root

if __name__ == "__main__":
    root=root()
    root.mainloop()
