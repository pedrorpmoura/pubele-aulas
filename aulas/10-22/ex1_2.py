
from re import *
import sys

def ex2(palavra):

	with open('dicionario_medico_novo.txt') as f:

		content = f.readlines() #retorna lista com as linhas do ficheiro
		num_oco = 0
		linhas = []
		for i,line in enumerate(content):
			matches = findall(rf"(?i:\b{palavra}\b)",line) #lista com todas as ocorrências da palavra na linha
			

			line = line.rstrip()
			line = sub(rf"(?i:\b({palavra})\b)",r"<b>\1</b>",line)

			if matches: #se houver match na linha
				num_oco += len(matches)
				linhas.append(line) #guarda a linha
		for l in linhas:
			print(f"<p>{l}</p>\n")
		print("Número total de ocorrências da palavra " + palavra +": ", num_oco)


def main():

    palavra = sys.argv[-1]
    ex2(palavra)
  
main()

