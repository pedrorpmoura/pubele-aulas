#!/usr/bin/python3 

from re import *
import sys

cabecalho = '''<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE xdxf SYSTEM "https://raw.github.com/soshial/xdxf_makedict/master/format_standard/xdxf_strict.dtd">
<xdxf lang_from="POR" lang_to="POR" format="logical" revision="033">
    <meta_info>
        <title>Dicionario_medico</title>
        <full_title>Dicionário Médico</full_title>
        <description> ... </description>
        <file_ver>001</file_ver>
    </meta_info>
    <lexicon>'''

#entrada :  <ar><k>entrada</k><def></def></ar>


def transforma_dic(dic):

    with open(dic) as f:
        content = f.read() 

    ## Limpa
    content = sub(r'\f','\n',content)
    content = sub(r'<','&lt;',content) # "<" "&lt;"       
    content = sub(r'>','&gt;',content) # ">" "&gt"; 
  
    ## Anotar artigos, keys, def
    entradas = split(r"\n{2,}",content)
    for entrada in entradas:
        nova = pros(entrada)
        print(f"<ar>{nova}</ar>")
            
def pros(entrada):
    entrada = sub(r"(^.*)",r"<k>\1</k><def>",entrada)
    return entrada +"</def>"
           
def main():
    print(cabecalho)
    transforma_dic(sys.argv[1])
    print("</lexicon>")
    print("</xdxf>")

main()
