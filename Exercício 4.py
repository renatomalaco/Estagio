def numeros_impares(n):
    num = 1 
    impares = []
    
    for i in range(n):
        impares.append(num)
        num += 2
    
    return impares

resultado_a = numeros_impares(5)     

def dobro_de_pares(n):
    num = 2
    dobro = []
    
    for i in range(n):
        dobro.append(num)
        num *= 2
        
    return dobro
    
resultado_b = dobro_de_pares(7)

def sequencia_soma_impares(n):
    soma = 0
    impares = numeros_impares(n)
    sequencia = []
    
    for num in impares:
        sequencia.append(soma)
        soma += num
        
    return sequencia
        
resultado_c = sequencia_soma_impares(8)

def raiz_de_pares(n):
    num = 2
    sequencia = []
    
    for i in range(n):
        par = num + 2
        num *= num 
        sequencia.append(num)
        num = par
        
    return sequencia 
    
resultado_d = raiz_de_pares(5)

def fibonacci(n):
    a, b = 0, 1 
    sequencia = []
    
    for i in range(n):
        a, b = b, a + b
        sequencia.append(a)
        
    return sequencia 
    
resultado_e = fibonacci(7)

def proximo_sequencia():
    sequencia = [2, 10, 12, 16, 17, 18, 19]
    ultimo_numero = sequencia[-1]
    
    proximo = ultimo_numero + 1
    
    if ultimo_numero % 2 != 0:  
        while proximo % 2 != 0:
            proximo += 1 
            
    sequencia.append(proximo)
        
    return sequencia
    
resultado_f = proximo_sequencia()

print(f"a) {resultado_a}")
print(f"b) {resultado_b}")
print(f"c) {resultado_c}")
print(f"d) {resultado_d}")
print(f"e) {resultado_e}")
print(f"f) {resultado_f}")
