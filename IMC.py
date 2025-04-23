altura = float(input("Insira sua altura: "))
peso = float(input("Insira seu peso em KG: "))
IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f"IMC:{IMC} está abaixo do normal!")
elif IMC > 24.9:
    print(f"IMC:{IMC} está acima do normal!")
else:
    print(f"IMC: {IMC:.2f} está dentro do normal!")