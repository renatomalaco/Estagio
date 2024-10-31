def eh_fibonacci(num):
    # Inicia a sequência de Fibonacci
    a, b = 0, 1
    # Verifica se o número informado é 0 ou 1, que estão na sequência
    if num == 0 or num == 1:
        return f"O número {num} pertence à sequência de Fibonacci."
    
    # Gera a sequência de Fibonacci até o número informado
    while b < num:
        a, b = b, a + b
    
    # Verifica se o número está na sequência
    if b == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
print(eh_fibonacci(numero))
