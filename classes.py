class Conta():
    def __init__(self, nome, data_nsc, email, senha):
        self.nome = nome
        self.data_nsc = data_nsc
        self.email = email
        self.senha = senha

#lembra de passar a conta como argumento
class Perfil(Conta):
    def __init__(self, nome, data_nsc, escola):
        super().__init__(nome, data_nsc, email=None, senha=None)
        self.escola = escola

class Atividade():
    def __init__(self, info, disciplina, data_entrega, arquivo):
        self.info = info
        self.disciplina = disciplina
        self.data_entrega = data_entrega
        self.arquivo = arquivo
