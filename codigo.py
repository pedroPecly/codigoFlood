import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import Entry, Button, Label

def digitar_texto_rapido(texto, velocidade, tempo=None):
    time.sleep(5)
    tempo_inicial = time.time()
    
    while True:
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial
        
        pyautogui.typewrite(texto, interval=0.01)

        pyautogui.press('enter')

        time.sleep(velocidade)
        
        if tempo is not None and tempo_decorrido >= tempo:
            print("Tempo esgotado.")
            break
        
        if keyboard.is_pressed('='):
            print("Parou")
            break

def iniciar_digitar():
    texto = entrada_texto.get()
    velocidade = float(entrada_velocidade.get())
    tempo_str = entrada_tempo.get()
    
    if tempo_str.strip() == "":
        digitar_texto_rapido(texto, velocidade)
    else:
        tempo = float(tempo_str)
        digitar_texto_rapido(texto, velocidade, tempo)

root = tk.Tk()
root.title("Encherdor de saco")

label_velocidade = Label(root, text="Velocidade:")
label_velocidade.pack(pady=5)
entrada_velocidade = Entry(root, width=40)
entrada_velocidade.pack(pady=10)

label_tempo = Label(root, text="Tempo:")
label_tempo.pack(pady=5)
entrada_tempo = Entry(root, width=40)
entrada_tempo.pack(pady=5)

label_texto = Label(root, text="Texto:")
label_texto.pack(pady=5)
entrada_texto = Entry(root, width=40)
entrada_texto.pack(pady=10)

botao_iniciar = Button(root, text="Iniciar", command=iniciar_digitar)
botao_iniciar.pack(pady=10)

root.mainloop()
