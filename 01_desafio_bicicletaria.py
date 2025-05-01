
class Bicicleta:
    def __init__(self, cor, Modelo, ano, valor, marcha=1):
        self.cor = cor
        self.Modelo = Modelo
        self.ano = ano
        self.valor = valor
        self.marcha = marcha

    
    def buzinar(self):
        print("BiiiiiBiiiiii...!")
    
    def parar(self):
        print("parando Bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuuuuum...!") 
    
    def trocar_marcha(self):
        nova_marcha = int(input("Insira qual marcha deseja trocar: "))
        if 1 <= nova_marcha<= 10:
           self.marcha = nova_marcha
           print(f"Marcha trocada para {self.marcha}!")
        else:
            print("Marcha inválida. Tente um valor entre 1 e 10.")

           
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2020, 600) 

print(b1)
b1.buzinar()
b1.parar()
b1.correr()
b1.trocar_marcha()

b2 = Bicicleta("Verde", "Sense", 2024, 400)

print(b2)
b2.buzinar()
b2.parar()
b2.correr()
b2.trocar_marcha()


































