import re
import sys


def parse_file(filename):

    res = dict()

    with open(filename, 'r') as f:

        #content = f.readlines()
        content = f.read().splitlines()
        content = content[3:]

        in_def = False
        word = ''
        for line in content:
            if line != '':
                if not in_def:
                    word = line
                    res[word] = []
                    in_def = True
                else:
                    res[word].append(line)
            else:
                in_def = False

    return res


def search(word, dictionary):

    for key, value in dictionary.items():
        value = ' '.join(value)
        if word in key or word in value:
            print(key + ' :: ' + value)


def main():

    filename = 'dicionario_medico_formatado.txt'

    word = sys.argv[-1]

    dicionario = parse_file(filename)
    search(word, dicionario)



if __name__ == '__main__':
    main()