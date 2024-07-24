class Livro:
    def __init__(self, titulo: str, autor: str, genero: str, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponivel = disponivel

    def __str__(self):
        return f"Titulo: {self.titulo} \nAutor: {self.autor} \nGenero: {self.genero}"
