#!/usr/bin/python3

"""
 Processa dicionário médico 
   extrai - lista dos verbetes
   extrai - lista de pares verbetes, def
"""

from re import *

with open("dicionario_medico.txt", "r") as f:

    content = f.read()

    content = sub(r'\f'  , '\n' , content)  ### retirar quebras de página
    content = sub(r'\n\n', '\n@', content)  ### linha em branco → @verbete 

    verbetes = findall(r'@(.*)',       content)
    print(verbetes)
    verb_def = findall(r'@(.*)\n(.*)', content)
    print(verb_def)
