# 1.Desarrolle en alg´un lenguaje de programaci´on el algoritmo de b´usqueda binaria 
def binary_search(lista,x):

    low = 0
    high = len(lista) -1
    mid = 0

    while low <= high:
        mid = (low + high)//2
        if lista[mid] < x:  # Si x es mayor, ignora el lado izquierdo >-
            low = mid + 1
        elif lista[mid] > x : # Si x es menor , ignora el lado derecho ->
            high = mid - 1
        else:
            return mid
    return -1

array = [1,2,4,7,9,10,11]
print(binary_search(array,11))