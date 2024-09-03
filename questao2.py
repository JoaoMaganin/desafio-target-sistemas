def pertence_fibonacci(n):
    # Inicializa os primeiros dois números da sequência
    a, b = 0, 1
    
    # Caso o número informado seja 0 ou 1, sabemos que ele pertence à sequência
    if n == 0 or n == 1:
        return True
    
    # Gera a sequência de Fibonacci até que o número seja maior ou igual ao número informado
    while b < n:
        a, b = b, a + b
    
    # Verifica se o número informado está na sequência
    return b == n

try:
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
except ValueError:
    print("Por favor, insira um número válido.")

# Verifica se o número pertence à sequência e exibe a mensagem correspondente
if pertence_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
