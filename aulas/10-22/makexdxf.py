cabecalho = '''<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE xdxf SYSTEM "https://raw.github.com/soshial/xdxf_makedict/master/format_standard/xdxf_strict.dtd">
<xdxf lang_from="POR" lang_to="POR" format="logical" revision="033">
    <meta_info>
        <title>Dicionario_medico</title>
        <full_title>Webster's Unabridged Dictionary</full_title>
        <description>Webster's Unabridged Dictionary published 1913 by the Webster Institute</description>
        <file_ver>001</file_ver>
    </meta_info>
    <lexicon>'''

        #<ar>
            #<k>entrada</k>
            #<def>
                #</def>
        #</ar>
from re import *
import sys

def transforma_dic(dic):

    with open(dic) as f:

        content = f.read() 
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