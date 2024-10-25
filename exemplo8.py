# Seu código aqui
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

escolha = input("Digite 'C' para converter de Celsius para Fahrenheit, ou 'F' para o contrário: ")
temperatura = float(input("Digite a temperatura: "))

if escolha.upper() == 'C':
    resultado = celsius_para_fahrenheit(temperatura)
    print(f"{temperatura}°C é igual a {resultado:.2f}°F")
elif escolha.upper() == 'F':
    resultado = fahrenheit_para_celsius(temperatura)
    print(f"{temperatura}°F é igual a {resultado:.2f}°C")
else:
    print("Escolha inválida. Por favor, digite 'C' ou 'F'.")