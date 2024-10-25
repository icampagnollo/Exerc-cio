numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para terminar): ")
    if entrada.lower() == 'fim':
        break
    numeros.append(float(entrada))

if numeros:
    media = sum(numeros) / len(numeros)
    print(f"A média dos números é: {media}")
else:
    print(f"Nenhum número foi inserido.")