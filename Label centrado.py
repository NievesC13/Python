import tkinter as tk

root = tk.Tk()

# Creamos un Label con un texto
label = tk.Label(root, text="Este es un Label centrado")
label.pack(side="top", fill="both", expand=True)

root.mainloop()