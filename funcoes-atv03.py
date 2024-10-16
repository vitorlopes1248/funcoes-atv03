# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

raio = float(input("Digite o raio do circulo:"))
area = 3.14 * (raio **2)
def calcular_area_base(area):
    return area
re=calcular_area_base(area)
print(re)

altura = float(input("Digite a altura: "))

def calcular_volume_cilindro(altura):
    volume = area * altura
    return volume

al=calcular_volume_cilindro(altura)
print(al)