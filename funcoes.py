def menu_loguin():
    from classes import Conta
    print('1 - Cadastrar conta')
    print('2 - Loguin')
    print('x - Sair')
    opcao = input('Digite a opção: ')

    if opcao == '1':
        usuario = Conta
        usuario.nome = input('Digite seu nome: ')
        usuario.idade = input('Digite sua idade: ')
        usuario.telefone = input('Digite seu telefone: ')
        usuario.endereco = input('Digite seu endereço: ')
        #log.email = input('Digite seu email: ')
        #log.senha = input('Digite sua senha: ')
        #banco.insert_user(usuario, log)
    if opcao == '2':
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        #if email in log.email and senha in log.senha:
        #    opc = ''
         #   while opc != 'x':
          #      opc = perfil.menu_feed(email, senha)
    return (opcao)

#deve-se impletar uma comunicação basica com o banco de dados
