class entrada:
    def entrar(self):
        while True:
            entradas = input('[E]ntrar\n[S]air: ')
            if entradas == 'E' or entradas == 'e' or entradas == 'S' or entradas == 's':
                return entradas
            else:
                print('Essa opção não existe.\nDigite uma opção válida! ("E" ou "S")')

entrada1 = entrada()
entradas = entrada1.entrar()

entradaE = entradas == 'E' or entradas == 'e'
entradaS = entradas == 'S' or entradas == 's'

senha_digitada = ''

class inicio:
    def versenha(self):
        senha_digitada = input('Senha: ')
        return senha_digitada

senha_permitida = '123456'
while True:
    if entradaE:
        iniciar = inicio()
        senha_digitada = iniciar.versenha()
        if senha_digitada == senha_permitida:
            print('Entrando...')
            break
        else:
            while True:
                print('Senha incorreta. Tente novamente.')
                senha_digitada = iniciar.versenha()
                if senha_digitada == senha_permitida:
                    print('Entrando...')
                    break
            break 
    elif entradaS:
        print('Saindo...')
        break
