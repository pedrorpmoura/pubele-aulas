from re import *
import sys


data_collections_path = '../../data-collections/'

def proc_entrada(entrada):
    entrada = sub(r'^(.+)\n((.|\n)+)', r'<k>\1</k><def>\2</def>, string)', entrada)


def transforma_dict():

    with open(data_collections_path + 'dicionario/dicionario_medico.txt') as f:
        content = f.read()
        entradas = split('\n{2,}', content)

        for entrada in entradas[1:10]:
            nova = proc_entrada(entrada)
            print(f'<ar>{entrada}</ar>')


print('''
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE xdxf SYSTEM "https://raw.github.com/soshial/xdxf_makedict/master/format_standard/xdxf_strict.dtd">
<xdxf lang_from="POR" lang_to="POR" format="logical" revision="033">
    <meta_info>
        <title>Webster's Dictionary</title>
        <full_title>Webster's Unabridged Dictionary</full_title>
        <description>Webster's Unabridged Dictionary published 1913 by the Webster Institute</description>
        <file_ver>001</file_ver>
    </meta_info>
    <lexicon>
''')

transforma_dict()

print('''
    </lexicon>
</xdxf>
''')






