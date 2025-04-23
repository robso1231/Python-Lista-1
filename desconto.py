desconto = int(input("Digite a porcentagem de desconto: "))
valor = float(input("Digite o valor a ser calculado: "))
porcentagem = desconto / 100
final = valor - (valor * porcentagem)

print (f"O valor com desconto é: {final}")