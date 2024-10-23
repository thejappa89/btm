def leiaint(caracteres):
    while True:
        try:
            num = int(input(caracteres))
        except (ValueError, TypeError):
            print('ERRO: Por favor, digite um número inteiro válido')
        except KeyboardInterrupt:
            print('ERRO: Entrada interrompida pelo usuário.')
            return 0
        else:
            return num