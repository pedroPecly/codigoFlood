import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import Entry, Button, Label

def digitar_texto_rapido(texto, velocidade):
    time.sleep(5)

    while True:
        pyautogui.typewrite(texto, interval=0.01)

        pyautogui.press('enter')

        time.sleep(velocidade)
        
        if keyboard.is_pressed('='):
            print("Parou")
            break

def iniciar_digitar():
    texto = entrada_texto.get()
    velocidade = entrada_velocidade.get()
    digitar_texto_rapido(texto, float(velocidade))

root = tk.Tk()
root.title("Encherdor de saco")


label_velocidade = Label(root, text="Velocidade:")
label_velocidade.pack(pady=5)
entrada_velocidade = Entry(root, width=40)
entrada_velocidade.pack(pady=10)

label_texto = Label(root, text="Texto:")
label_texto.pack(pady=5)
entrada_texto = Entry(root, width=40)
entrada_texto.pack(pady=10)

botao_iniciar = Button(root, text="Iniciar", command=iniciar_digitar)
botao_iniciar.pack(pady=10)

root.mainloop()
