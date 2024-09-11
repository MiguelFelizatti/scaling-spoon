def pertence_fibonacci(n):
    if n < 0:
        return False
    
    # Função para gerar números de Fibonacci
    def fibonacci_sequence_up_to(limit):
        fib_sequence = [0, 1]
        while True:
            next_value = fib_sequence[-1] + fib_sequence[-2]
            if next_value > limit:
                break
            fib_sequence.append(next_value)
        return fib_sequence
    
    # Gera a sequência de Fibonacci até o número informado
    fib_sequence = fibonacci_sequence_up_to(n)
    
    # Verifica se o número está na sequência
    if n in fib_sequence:
        return True
    else:
        return False

# Solicita ao usuário para informar um número
try:
    numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
    
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, insira um número inteiro válido.")