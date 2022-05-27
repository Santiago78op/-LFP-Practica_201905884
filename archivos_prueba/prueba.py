
lista = [["\"zapatos\"",22,65],["blusas",25,88],["lavadora",58,19]]

lista_1 = []

for i in lista:
    datos = i
    total = datos[1] * datos[2]
    lista_1.append([datos[0],datos[1],datos[2],total])
    
img = dict()
img["Productos"]=lista_1
contenido = img["Productos"]
contenido[0][0].replace('\"','')
#print(img)

print(contenido[0])
print(contenido[-1])