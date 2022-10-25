# coletando dados do usuario
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
altura = float(input("digite sua altura: "))
peso = float(input("digite sua peso: "))
IMC = peso/altura**2

print("-" * 30)
print("Os Dados coletados foram:")
print("nome: ", nome)
print("idade: ", idade, " anos")
print("altura: ", altura)
print("peso: ", peso," quilos")
print("IMC: ", IMC)