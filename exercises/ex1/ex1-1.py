import re


with open("dicionario_medico.txt", "rw") as f:

    content = f.read()
    new_content = re.sub('\x0c', '\n', content)

    print(new_content)


