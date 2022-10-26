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

if IMC < 16:
    print("Magreza Grave! Cuidado!!")
elif IMC < 18.5:
    print("Magreza leve! Abaixo do peso normal.")
elif IMC < 24.9:
    print("Peso normal. Parabéns!")
elif IMC < 29.9:
    print("Excesso de peso. Cuidado!")
elif IMC < 34.9:
    print("Obesidade classe I. Cuidado em!")
elif IMC < 39.9:
    print("Obesidade classe II. Tá só piorando!!")
else:
    print("Obesidade classe III. Meu Deusss!!!!!!")