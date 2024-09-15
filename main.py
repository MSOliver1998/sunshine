import tkinter as tk
from tela import tela

def root():
    root= tk.Tk()
    root.geometry("600x600")
    root.title("Sunshine") 
    tela(root)
    return root
    

if __name__ == "__main__":
    root=root()
    root.mainloop()
