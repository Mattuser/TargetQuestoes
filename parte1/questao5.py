string = 'Batatinha'
array = list(string)
contador = 0
lista_final = []
while contador < len(array):
    lista = array.pop()
    lista_final.append(lista)

string_final = "".join(lista_final)

print(string_final) #ahnitataB


