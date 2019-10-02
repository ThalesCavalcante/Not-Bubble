# LARISSA TENORIO E THALES VALDSON

from random import shuffle

def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista



def not_bubble_sort(lista):
    elementos = len(lista)/2
    ordenado = False
    ordenado2= False
    while not ordenado:
        ordenado = True
        for i in range(int(elementos)):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                ordenado = False

    while not ordenado2:
        ordenado2 = True
        for i in range(len(lista)-1,int(elementos),-1):
            if lista[i] < lista[i - 1]:
                lista[i], lista[i - 1] = lista[i - 1], lista[i]
                ordenado2 = False

    lista1=lista[:int(elementos)]
    lista2=lista[int(elementos) :]

    final = []
    while lista1 or lista2:
        if len(lista1) and len(lista2):
            if lista1[0] < lista2[0]:
                final.append(lista1.pop(0))
            else:
                final.append(lista2.pop(0))
        if not len(lista1):
            if len(lista2): final.append(lista2.pop(0))
        if not len(lista2):
            if len(lista1): final.append(lista1.pop(0))

    return final



size = [10, 20, 30]
time = []

for s in size:
    lista = geraLista(s)
    print('Nao ordenada: ', lista)
    ordenada = not_bubble_sort(lista)
    print('Ordenada: ', ordenada)
    print('\n')
