class Conta():
    def __init__(self, nome, email, senha, escola):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.escola = escola

    def get_nome(self):
        return self.nome


    def get_email(self):
        return self.email

    def get_senha(self):
        return self.senha

    def get_escola(self):
        return self.escola

    def set_escola(self,novo_escola):
        self.escola = novo_escola

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_senha(self,nova_senha):
        self.senha = nova_senha

        
class Atividade():
    def __init__(self, info, disciplina, data_entrega, arquivo, tag):
        self.info = info
        self.disciplina = disciplina
        self.data_entrega = data_entrega
        self.arquivo = arquivo
        self.tag = tag
