class Carro:
    # Método construtor
    def __init__(self, marca, modelo):
        self.marca = marca   # Atributo
        self.modelo = modelo # Atributo

    # Método (comportamento)
    # O self representa a instância específica do objeto que está executando 
    # o método naquele momento.
    def buzinar(self):
        print(f"BEEP! O {self.modelo} está buzinando.")

# Criando um objeto (instância)
meu_carro = Carro("Toyota", "Corolla")
meu_carro.buzinar() # Saída: BEEP! O Corolla está buzinando.
