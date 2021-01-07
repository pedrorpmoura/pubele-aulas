import shelve



def find_all():
    with shelve.open('pessoas.db') as s:
        r = []
        for chave in s:
            nome = s[chave]['nome']

            d = { 'numero': chave, 'nome': nome}
            r.append(d)

        return r


def insert(data):
    """
    {
        "numero": numero
        "nome": nome
        "idade": idade
        "sexo": sexo
        "curso": curso
    }
    """

    with shelve.open('pessoas.db') as s:
        n = data.pop('numero')
        s[n] = data














