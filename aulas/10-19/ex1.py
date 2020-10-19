#!/usr/bin/python3

"""
 Processa dicionário médico: gera html
"""

from re import *

with open("dicionario_medico.txt", "r") as f:

    content = f.read()

    content = sub(r'\f', '\n', content)     ### retirar quebras de página
    content = sub(r'\n\n', '\n@', content)  ### linha em branco

    content = sub(r'@(.*)', r'<hr/><b>\1</b><br/>', content)  ### linha em branco
    content = "<h1>Dicionário médico</h1>" + content

    with open("dicionario_medico_formatado.html", "w") as o:
        o.write(content)

"""
abaixador de língua
Instrumento para abaixar a língua, no exame da garganta; abaixa-língua; cataglosso.

abalado
Que sofreu abalo; deprimido.
"""
