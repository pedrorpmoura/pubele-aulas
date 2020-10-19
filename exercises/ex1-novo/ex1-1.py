import re



#with open("dicionario_medico.txt", "r") as f:
#    
#    lines = f.readlines()
#
#    with open("dicionario_medico_2.txt", "w") as o:
#        for line in lines:
#            found = line.find('\x0c')
#            if found != -1:
#                line = '\n' + line[1:]
#                o.write(line)
#
#                # o.write('\n')
#                # o.write(line[1:])
#            else:
#                o.write(line)


with open("dicionario_medico.txt", "r") as f:

    content = f.read()
    new_content = re.sub('\x0c', '\n', content)

    with open("dicionario_medico_formatado.txt", "w") as o:
        o.write(new_content)
