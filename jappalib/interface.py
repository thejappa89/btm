from myfuncs import leiaint


def linha(tam=42, caracter='-'):
    print(tam * caracter)


def titulo(txt, tam=42, caracter='-'):
    linha(tam, caracter)
    print(txt.center(tam))
    linha(tam, caracter)


def menu(lista, msg='MENU PRINCIPAL'):
    titulo(msg)
    for e, i in enumerate(lista):
        print(f'{e + 1}. {i}')
    linha()
    opc = leiaint('Sua opção: ')
    return opc
    linha()
