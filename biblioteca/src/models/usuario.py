import uuid

class Usuario:
    def __init__(self, nome: str):
        self.id = str(uuid.uuid4())
        self.nome = nome

    def __str__(self):
        return f"ID: {self.id} \nNome: {self.nome}"