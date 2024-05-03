class ValidadorCPF:
    def __init__(self, cpf):
        self.cpf = self._limpar_cpf(cpf)

    def _limpar_cpf(self, cpf):
        return ''.join(filter(str.isdigit, cpf))

    def _calcular_digitos_verificadores(self, cpf_parcial):
        def calcular_digito(cpf_parcial):
            soma = sum((len(cpf_parcial) + 1 - i) * int(digito) for i, digito in enumerate(cpf_parcial))
            digito = 11 - (soma % 11)
            return str(digito) if digito < 10 else '0'

        digitos_verificadores = ''
        for i in range(2):
            digitos_verificadores += calcular_digito(cpf_parcial)
            cpf_parcial += digitos_verificadores[-1]
        return digitos_verificadores

    def validar(self):
        if len(self.cpf) != 11 or self.cpf == self.cpf[0] * 11:
            return False

        cpf_parcial = self.cpf[:9]
        digitos_verificadores = self._calcular_digitos_verificadores(cpf_parcial)
        return digitos_verificadores == self.cpf[9:]

def main():
    cpf = input("Digite o CPF (somente números): ")
    validador = ValidadorCPF(cpf)
    if validador.validar():
        print("CPF válido.")
    else:
        print("CPF inválido.")

if __name__ == "__main__":
    main()
