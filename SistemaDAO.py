from Conta import Conta
class SistemaDAO:
    def __init__(self,conexao):
        self.conexao = conexao

    def inserir(self,nome,data_nasc,email,senha,escola):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO contas(nome,data_nasc,email,senha,escola) VALUES(%s,%s,%s,%s,%s)",(nome,data_nasc,email,senha,escola))
        cursor.close()
        self.conexao.commit()

    def logar(self,email,senha):
        cursor = self.conexao.cursor()
        cursor.execute

    def criar_atividade(self,info,disciplina,data_entrega,arquivo,TAG):
        cursor = self.conexao.cursor()
        cursor.execute("INSERT INTO atividades(info,disciplina,data_entrega,arquivo,TAG) VALUES(%s,%s,%s,%s,%s)",(info,disciplina,data_entrega,arquivo,TAG))


