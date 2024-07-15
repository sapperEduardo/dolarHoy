import os
import shutil
import requests 
from bs4 import BeautifulSoup 


dominio = 'https://dolarhoy.com/'





def get_list_prices():
    cod_fuente = requests.get(dominio).text
    soup = BeautifulSoup(cod_fuente, 'html.parser')
    return soup.find_all(class_='val')




def get_dict_prices():
    lista = get_list_prices()

    lista = [p.text[:5] for p in get_list_prices()]

    return dict({
        'Blue': (lista[0], lista[1]),
        'Oficial': (lista[4], lista[5]),
        'Bolsa': (lista[6], lista[7]),
        'CCL': (lista[8], lista[9]),
        'Cripto': (lista[10], lista[11]),
        'Tarjeta': ('--', lista[12]),
        })


