import tkinter as tk
from tkinter import simpledialog, messagebox, Menu, Text, Button
import base64
import pyperclip # Importar la librería pyperclip para copiar al portapapeles 
#hay que instalarla con pip install pyperclip

me
# Función para cifrar el mensaje usando el cifrado César
def cifrar_cesar(mensaje, clave):
    cifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            offset = clave % 26
            if caracter.islower():
                # Para minúsculas
                cifrado += chr((ord(caracter) - ord('a') + offset) % 26 + ord('a'))
            else:
                # Para mayúsculas
                cifrado += chr((ord(caracter) - ord('A') + offset) % 26 + ord('A'))
        else:
            cifrado += caracter
    return cifrado

# Función para convertir texto a binario, hexadecimal y Base64
def convertir_formatos(texto):
    binario = ' '.join(format(ord(i), 'b') for i in texto)
    hexadecimal = texto.encode().hex()
    base64_encoded = base64.b64encode(texto.encode()).decode()
    return binario, hexadecimal, base64_encoded

# Función para descifrar el mensaje cifrado en Base64 usando César
def descifrar_cesar(mensaje_base64, clave):
    mensaje = base64.b64decode(mensaje_base64).decode()
    descifrado = ""
    for caracter in mensaje:
        if caracter.isalpha():
            offset = clave % 26
            if caracter.islower():
                # Para minúsculas
                descifrado += chr((ord(caracter) - ord('a') - offset) % 26 + ord('a'))
            else:
                # Para mayúsculas
                descifrado += chr((ord(caracter) - ord('A') - offset) % 26 + ord('A'))
        else:
            descifrado += caracter
    return descifrado

# Función para mostrar resultados en una ventana de texto que permite copia y agregar botón de copia
def mostrar_resultados(titulo, contenido, base64_text=""):
    resultado_win = tk.Toplevel()
    resultado_win.title(titulo)
    text_area = Text(resultado_win, height=10, width=50)
    text_area.pack()
    text_area.insert(tk.END, contenido)
    text_area.config(state=tk.DISABLED)  # Desactivar edición pero permitir copia
    
    if base64_text:
        def copiar_base64():
            pyperclip.copy(base64_text)
            messagebox.showinfo("Copiado", "Mensaje en Base64 copiado al portapapeles.")
        
        Button(resultado_win, text="Copiar Base64", command=copiar_base64).pack()

# Función para crear y mostrar la ventana de cifrado
def mostrar_ventana_cifrado():
    mensaje = simpledialog.askstring("Cifrado César", "Ingrese el mensaje a cifrar:")
    if mensaje is None: return
    clave = simpledialog.askinteger("Cifrado César", "Ingrese la clave de cifrado:")
    if clave is None: return
    cifrado = cifrar_cesar(mensaje, clave)
    binario, hexadecimal, base64_encoded = convertir_formatos(cifrado)
    resultado = f"Binario: {binario}\nHexadecimal: {hexadecimal}\nBase64: {base64_encoded}"
    mostrar_resultados("Mensaje Cifrado", resultado, base64_encoded)

# Función para crear y mostrar la ventana de descifrado
def mostrar_ventana_descifrado():
    mensaje_base64 = simpledialog.askstring("Descifrado César", "Ingrese el mensaje cifrado en Base64:")
    if mensaje_base64 is None: return
    clave = simpledialog.askinteger("Descifrado César", "Ingrese la clave de cifrado:")
    if clave is None: return
    descifrado = descifrar_cesar(mensaje_base64, clave)
    mostrar_resultados("Mensaje Descifrado", f"Texto ASCII: {descifrado}")

# Crear la ventana principal
root = tk.Tk()
root.title("Cifrado y Descifrado César")

# Crear menú
menu = Menu(root)
root.config(menu=menu)
menu_cifrado = Menu(menu, tearoff=0)
menu.add_cascade(label="Cifrar", menu=menu_cifrado)
menu_cifrado.add_command(label="Cifrar Mensaje", command=mostrar_ventana_cifrado)

menu_descifrado = Menu(menu, tearoff=0)
menu.add_cascade(label="Descifrar", menu=menu_descifrado)
menu_descifrado.add_command(label="Descifrar Mensaje", command=mostrar_ventana_descifrado)

# Ejecutar la aplicación
root.mainloop()