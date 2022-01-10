def pertence(n):
    i = 0
    j = 1
    resultado = int()
    
    while resultado < n:
        resultado = i + j 
        i = j
        j = resultado

    if(n == resultado):
        return f'Pertence {n}'

    else:
        return f'Não pertence {n}'   



print(pertence(6))
print(pertence(21))
print(pertence(13))
print(pertence(7))
print(pertence(0))
