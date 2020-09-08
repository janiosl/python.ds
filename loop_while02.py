tecnologias = ['Python', 'Machine Learning', 'RPA', 'Web']

while True:
    tecnologia = input('Digite um termo relacionado a tecnologia: ')

    if tecnologia in tecnologias:
        print('Esta tecnologia está em nossa lista')
    else:
        print('Esta tecnologia não está em nossa lista')

    continuar = input('Deseja continuar [S/N]? ')[0].upper()

    if continuar == 'N':
        break
