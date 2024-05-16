valor_saque = int (input("digite o valor do saque: "))

notas = [50, 20, 10, 5]
quantidade_notas = {}


for nota in notas:
    quantidade_notas[nota], valor_saque = divmod(valor_saque, nota)

print("quantidade de notas para o saque: ")
for nota, quantidade in quantidade_notas.items():
    if quantidade > 0:
        print(f"notas de R$ {nota}: {quantidade}")
        