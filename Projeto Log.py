with open('Log_registro.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('\n---INÍCIO DO LOG---\n')

def senhaConta():
    senha = input('Digite a senha para se registrar: ')
    return senha

def usuarioConta():
    usuario = input('Digite o usuario para se registrar: ')
    return usuario

def repeticaoSenha():
    repSenha = input('Repita a senha para confirmar seu cadastrado: ')
    return repSenha

print('Bem-vindo, ao controle de sua conta!!')
print('Hora de fazer seu registro de conta \n')
print('=-='*40)
usuario = usuarioConta().lower()
senha = senhaConta()
repSenha = repeticaoSenha()
print('=-='*40)

while True:

    if repSenha != senha:
        print('As senhas não são iguais, tente novamente')
        senha = senhaConta()
        repSenha = repeticaoSenha()
    else:
        print('Conta criada com sucesso!!')
        break

print('Agora faça login em sua conta.\n')

usuarioExistente = input('Digite seu usuário: ').lower()
senhaExistente = input('Digite sua senha: ')
print('=-='*40)
contador = 5

while True:
    if usuarioExistente != usuario:
        print('Esse usuário não existe, tente novamente.')
        usuarioExistente = input('Digite seu usuário: ').lower()
    
    elif senhaExistente != senha:
        contador -= 1
        
        print('Senha incorreta!!, tente novamente.')
        senhaExistente = input('Digite sua senha: ')
        print(f'As tentativas de login são limitadas, restão {contador} tentativas.')
        
        if contador <= 0:
            print('Suas tentivas chegaram ao limite, pela sua segurança estamos bloqueando suas tentativas por um determinado tempo.')
            break
    else:
        usuarioExistente == usuario and senhaExistente == senha
        loginCompleto = print('Seu login foi feito com sucesso!!')
        break

from datetime import date, datetime
dataLog = datetime.now().strftime('%H:%M:%S')


print('=-='*40)
with open('Log_registro.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write(F'O login feito em {dataLog}\n')

def listaFuncao():
    print('[1]- Abrir LOG de login')
    print('[2]- Deslogar da conta')
    resposta = input('Digite a opção de sua escolha: ')
    return resposta



while True:
    opcao1 = listaFuncao()
    print('=-='*40)
    if opcao1 == '1':
        with open('Log_registro.txt', 'r', encoding='utf-8') as arquivo:
            leitura = arquivo.read()
            print(leitura)
            print('=-='*40)

    elif opcao1 == '2':
        print('Obrigado por usar nossos serviços!!')
        print('Conta deslogada.')
        break
    else:
        print('Opção invalida!!')

with open('Log_registro.txt', 'a', encoding='utf-8') as arquivo:
    dataDeslogue = datetime.now().strftime('%H:%M:%S')
    arquivo.write(f'Deslogamento da conta {dataDeslogue}\n')
