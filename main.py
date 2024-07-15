import os
import tkinter as tk
import customtkinter as ctk

from cotizaciones import get_dict_prices

ctk.set_default_color_theme('green')


dict_precios = dict()
nombres_tipos = ['Blue','Oficial','Bolsa','CCL','Cripto','Tarjeta']

# actualiza el dicionario de precios con los actuales
def update_prices():
    global dict_precios
    dict_precios = get_dict_prices()
    put_prices(tipo_cambio.get())
    root.after(300000, update_prices)

# pone los precios en las etiquetas
def put_prices(tipo): 
    compra, venta = dict_precios[tipo] 
    valor_compra.set(compra)
    valor_venta.set(venta)

# cambia a la cotizacion anterior 
def previus_price():
    tipo_actual = tipo_cambio.get()
    i = nombres_tipos.index(tipo_actual)
    tipo = nombres_tipos[i - 1] 
    tipo_cambio.set(tipo)
    put_prices(tipo)

# cambia a la cotizacion siguiente 
def next_price():
    tipo_actual = tipo_cambio.get()
    i = nombres_tipos.index(tipo_actual)
    tipo = nombres_tipos[i + 1] if i < 5 else 'Blue'
    tipo_cambio.set(tipo)
    put_prices(tipo)

# cambia el tipo y su cotizacion dependiendo de la tecla/flecha presionada
def tecla_flecha(event):
    next_price() if event.keysym == 'Right' else previus_price()



root = ctk.CTk()
root.title('dolarhoy')
root.geometry('240x133+1500+40')
root.resizable(False, False)

root.iconbitmap('C:\\dolarhoy\\ico\\icono.ico')

# Variables (Tipo cambio, compra, venta y fuentes)
tipo_cambio = ctk.StringVar(None, 'Blue')
valor_compra = ctk.DoubleVar()
valor_venta = ctk.DoubleVar()
f1 = 'Sitka Small'
f2 = 'Yu Gothic UI'
f3 = 'Segoe UI'
f4 = 'Terminal'

# Parte superior
frame_superior = ctk.CTkFrame(root)

previus_button = ctk.CTkButton(frame_superior, text='<', font=(f4,30), width=14, height=17, command=previus_price)
previus_button.grid(column=0, row=0, padx= 15, pady= 10)

etiqueta_tipo = ctk.CTkLabel(frame_superior, textvariable=tipo_cambio, font=(f1,22,'bold'), width=80)
etiqueta_tipo.grid(column=1, row=0, padx = 12, pady= 10)

next_button = ctk.CTkButton(frame_superior, text='>', font=(f4,30), width=14, height=17, command=next_price)
next_button.grid(column=2, row=0, padx= 15, pady= 10)

frame_superior.pack()


# Parte inferior
frame_inferior = ctk.CTkFrame(root)

etiquetaC = ctk.CTkLabel(frame_inferior, text='Compra:', font=(f3, 18)).grid(column=0, row=0, padx=25)
etiquetaV = ctk.CTkLabel(frame_inferior, text='Venta:', font=(f3, 18)).grid(column=1, row=0, padx=25)

etiqueta_precio_C = ctk.CTkLabel(frame_inferior, textvariable=valor_compra, font=(f2,26)).grid(column=0, row=1, padx=18,pady=5)
etiqueta_precio_V = ctk.CTkLabel(frame_inferior, textvariable=valor_venta, font=(f2,26)).grid(column=1, row=1, padx=18,pady=5)

frame_inferior.pack()

update_prices()

put_prices('Blue')


# captar eventos (flechas left/right)
root.bind('<Left>', tecla_flecha)
root.bind('<Right>', tecla_flecha)



root.mainloop()

