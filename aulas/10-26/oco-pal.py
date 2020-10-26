#!/usr/bin/python3 

from re import *
import sys

conta_oco = {}
def oco(file):

    with open(file) as f:
        content = f.read() 

    ## Limpa

    for palavra in findall(r'\w+', content):
#        print(palavra)
        if palavra in conta_oco:
            conta_oco[palavra] += 1
        else: 
            conta_oco[palavra] = 1
    print(conta_oco)
 
oco(sys.argv[1])


"era uma vez uma árvore, uma galinha e um peru,"
    
"""
 [a-z]   a|b|...z
 \w      [a-zA-Z0-9_]    alfanumericos
 \W      tudo menos \w 
 \s      espaços, newline, tab
 \d      [0-9]
 .       tudo menos \n
 X*      repetições 0 ou mais
 X+      {1,}     {1,∞}
era => 1
uma => 3
...
"""
