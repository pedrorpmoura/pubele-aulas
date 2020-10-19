import os



def create_new_directory(path):

    if not os.path.isdir(path):
        os.makedirs(path)
        print('directory created')
    else:
        print('directory already exists')


def create_new_files():

    with open('dicionario_medico_3.txt', 'r') as f:
        

def main():

    create_new_directory('dicionarios')

    create_new_files()


if __name__ == '__main__':
    main()