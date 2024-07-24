from datetime import datetime

class Emprestimo:
    def __init__(self, nome_livro: str, nome_usuario: str, id_usuario: str, data_emprestimo: datetime, data_devolucao: datetime):
        self.nome_livro = nome_livro
        self.nome_usuario = nome_usuario
        self.id_usuario = id_usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
