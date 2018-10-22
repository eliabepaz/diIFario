from Sistema import Sistema
from Classe import Conta
class Menu:
    def __init__(self):
        pass
    def Menu(self):
        op = "-1"
        while op == "0":
            print("1 - Cadastrar conta")
            print ("0 - SAIR")
            op = input("escolha um numero")
        if op == "1":
            nome = input("Diga seu nome")
            email = input("diga seu email")
            senha = input("digite uma senha")
            escola = input("diga sua escola")
            criar_conta = Sistema(nome,email,senha,escola)
            criar_conta.criar_conta(nome,email,senha,escola)
