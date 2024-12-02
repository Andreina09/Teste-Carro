# Teste-Carro
Objetivos específicos:
Controle de estoque de carros: A revendedora pode adicionar carros à sua lista, representada pela classe Revendedora.

Limitação por marca: A revendedora não pode ter mais de 10 carros de uma mesma marca no estoque. Isso é verificado no método adicionar_carro(), que impede a adição de carros se já existirem 10 carros da mesma marca.

Contagem das marcas: O método contar_marcas() conta quantos carros de cada marca estão no estoque e ajuda a garantir que a limitação de 10 carros por marca seja respeitada.

Exibição do estoque: A revendedora pode listar todos os carros que foram adicionados ao seu estoque com o método listar_carros(), apresentando as marcas e os modelos.
Técnologiaa usadas:

Linguagem de Programação- Python
GitHub;
Visual Studio Code;

 Definição das Classes
   - *Classe Carro*: Esta classe é responsável por representar cada carro, com atributos como marca e modelo.
     python
     class Carro:
         def __init__(self, marca, modelo):
             self.marca = marca
             self.modelo = modelo
     
Classe Revendedora: Esta classe gerencia uma lista de carros, permitindo adicionar, listar e contar carros por marca.
     python
     class Revendedora:
         def __init__(self):
             self.carros = []
     
 Método para Adicionar Carros
adicionar_carro: Este método permite adicionar um carro à lista, verificando se o objeto é da classe Carro e se não excede o limite de 10 carros por marca.
     python
     def adicionar_carro(self, carro):
         if isinstance(carro, Carro):
             if self.contar_marcas().get(carro.marca, 0) < 10:
                 self.carros.append(carro)
                 print(f"Carro {carro.modelo} da marca {carro.marca} adicionado com sucesso.")
             else:
                 print(f"Erro: Já existem 10 carros da marca {carro.marca}.")
         else:
             print("Erro: O objeto não é um carro.")
     

Método para Contar Carros por Marca
contar_marcas: Este método percorre a lista de carros e conta quantos estão disponíveis de cada marca.
     python
     def contar_marcas(self):
         contagem_marcas = {}
         for carro in self.carros:
             contagem_marcas[carro.marca] = contagem_marcas.get(carro.marca, 0) + 1
         return contagem_marcas
     

Método para Listar Carros
listar_carros: Este método exibe todos os carros disponíveis na revendedora, informando marca e modelo.
     python
     def listar_carros(self):
         if not self.carros:
             print("Não há carros na revendedora.")
         else:
             for carro in self.carros:
                 print(f'Marca: {carro.marca}, Modelo: {carro.modelo}')
     

Exemplo de Uso
Após definir as classes, você cria uma instância da Revendedora, adiciona alguns carros e lista todos os carros disponíveis.
     python
     revendedora = Revendedora()
     revendedora.adicionar_carro(Carro("Toyota", "Corolla"))
     revendedora.adicionar_carro(Carro("Honda", "Civic"))
     
Resumo:
O código implementa uma revendedora de carros com a funcionalidade de adicionar carros ao estoque, respeitar um limite de 10 carros por marca e exibir os carros disponíveis para venda. A lógica ajuda a evitar o estoque e quantidade de carros dentro dessa revendedora.
