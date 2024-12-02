class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Revendedora:
    def __init__(self):
        self.carros = []

    def adicionar_carro(self, carro):
        # Verifica se o objeto é da classe Carro
        if isinstance(carro, Carro):
            # Conta quantos carros da mesma marca já existem
            if self.contar_marcas().get(carro.marca, 0) < 10:
                self.carros.append(carro)
                print(f"Carro {carro.modelo} da marca {carro.marca} adicionado com sucesso.")
            else:
                print(f"Erro: Já existem 10 carros da marca {carro.marca}.")
        else:
            print("Erro: O objeto não é um carro.")

    def contar_marcas(self):
        contagem_marcas = {}
        for carro in self.carros:
            contagem_marcas[carro.marca] = contagem_marcas.get(carro.marca, 0) + 1
        return contagem_marcas

    def listar_carros(self):
        # Lista todos os carros na revendedora
        if not self.carros:
            print("Não há carros na revendedora.")
        else:
            for carro in self.carros:
                print(f'Marca: {carro.marca}, Modelo: {carro.modelo}')

# Exemplo de uso
revendedora = Revendedora()
revendedora.adicionar_carro(Carro("Toyota", "Corolla"))
revendedora.adicionar_carro(Carro("Honda", "Civic"))
revendedora.adicionar_carro(Carro("Toyota", "Camry"))

# Adicionando mais carros para testar o limite de 10
for i in range(8):
    revendedora.adicionar_carro(Carro("Toyota", f"Modelo {i+1}"))

# Tentando adicionar um carro a mais da mesma marca para verificar a limitação
revendedora.adicionar_carro(Carro("Toyota", "Modelo Extra"))

# Listar todos os carros adicionados
print("\nLista de carros:")
revendedora.listar_carros()
