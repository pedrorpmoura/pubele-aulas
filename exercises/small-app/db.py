import shelve



def find_all():
    with shelve.open('proverbios.db') as s:
        return list(s.keys())


def find_one(proverbio):
    with shelve.open('proverbios.db') as s:
        return { 'proverbio': proverbio, 'significado': s[proverbio] }


def insert(proverbio_data):
    with shelve.open('proverbios.db', writeback=True) as s:
        s[proverbio_data['proverbio']] = proverbio_data['significado']
        return list(s.keys())