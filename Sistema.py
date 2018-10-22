import psycopg2
from Conta import Conta
from SistemaDAO import SistemaDAO
from Atividade import Atividade

class Sistema:
    def __init__(self,nome,data_nasc,email,senha,escola,info,disciplina,data_entrega,arquivo,TAG):
        Conta(nome,data_nasc,email,senha,escola)
        Atividade(info,disciplina,data_entrega,arquivo,TAG)
        conexao = psycopg2.connect(host="localhost", database="diIFario", user="postgres", password="1111")
        self.SistemaDAO = SistemaDAO(conexao)

    def criar_conta(self,nome,data_nasc,email,senha,escola):
        self.SistemaDAO.inserir(nome,data_nasc,email,senha,escola)

    def logar(self,email,senha):
        self.SistemaDAO.logar(email,senha)

    def criar_atividade(self,info,disciplina,data_entrega,arquivo,TAG):
        self.SistemaDAO.criar_atividade(info,disciplina,data_entrega,arquivo,TAG)
