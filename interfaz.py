from tkinter import *
import tkinter as interfz
from logic import button_click, validate_numb

def new_button(frame, fila, columna, color, size_button, texto, fuente, entry, result):
    boton = interfz.Button(frame, text=texto, relief="flat", bg=color,
                           command=lambda: button_click(texto, entry, result), font=fuente)
    boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)
    boton.config(width=size_button, height=size_button)

def create_ui():
    window = interfz.Tk()
    window.title("Calculadora chimba")
    window.geometry("600x400")
    window.configure(bg="black")
    window.iconbitmap("icon.ico")

    # Numbers label
    result_sector = interfz.Frame(window, height=100, width=475)
    result_sector.pack(fill="none", expand=False, pady=(10, 0)) 

    # Buttons label
    buttons = interfz.Frame(window, height=300, width=500, bg="black")
    buttons.pack(fill="none", expand=False, padx=10, pady=(10, 10)) 

    # Call validate numbers
    validacion = window.register(validate_numb)

    # Entry para los resultados
    entry = interfz.Entry(result_sector, width=12, font=("Arial", 50), justify=RIGHT,
                          validate="key", validatecommand=(validacion, '%S'))
    entry.pack(fill="none", expand=True)

    result = interfz.Entry(result_sector, width=30, justify=LEFT, font=("Arial", 20), state="readonly")
    result.pack(fill="none", expand=True)

    # Use arrays to graphic numbers
    buttons.grid_rowconfigure(0, weight=1)
    buttons.grid_columnconfigure(0, weight=1)
    buttons.grid_columnconfigure(1, weight=1)

    # label to first array (1-9)
    frame_buttons1 = interfz.Frame(buttons, bg="black")
    frame_buttons1.grid(row=0, column=0, sticky="nsew", padx=2, pady=5)
    font = ("Arial", 16)
    size = 5 
    for fila in range(3):
        frame_buttons1.grid_rowconfigure(fila, weight=1)
        for columna in range(3):
            texto_boton = str(fila * 3 + columna + 1)
            new_button(frame_buttons1, fila, columna, "gray", size, texto_boton, font, entry, result)

    # label to second array (0, +, -, *, /, %...)
    frame_botones2 = interfz.Frame(buttons, bg='black')
    frame_botones2.grid(row=0, column=1, sticky="nsew", padx=2, pady=5)
    textos_botones2 = [
        "+", "*", "AC", 
        "-", "/", "C",
        "0", "%", "="
    ]
    for fila in range(3):
        frame_botones2.grid_rowconfigure(fila, weight=1)
        for columna in range(3):
            texto_boton = textos_botones2[fila * 3 + columna]
            texto_color = "gray" if texto_boton == "0" else "orange"
            new_button(frame_botones2, fila, columna, texto_color, size, texto_boton, font, entry, result)

    window.mainloop()

if __name__ == "__main__":
    create_ui()
