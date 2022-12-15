from functools import reduce

def process_matrix(matrix):
    
    """
    process_matrix transforma los elementos de la matriz original.

    Recibe como parámetro una matriz (lista de listas) de números y
    devuelve otra, con el mismo tamaño y número de elementos.
    """
    if matrix == []: # caso trivial
        return []
    elif is_numerical_matrix(matrix): # caso correcto
        return _process_matrix(matrix)
    else:
    #error
        raise ValueError('Only works on numerical matrices')
   
 
def is_numerical_matrix(matrix):
    """Recibe una lista y devuelve True si y solo si:
    * matrix es una lista de listas
    * las sublistas son todas del mimso tamaño
    * el contenido de las sublistas es sólo numeros"""
    is_a_valid_matrix = True
    #comprobar que es una lista de listas 

    if not is_a_list_of_lists(matrix):
        is_a_valid_matrix = False
    elif not all_lists_are_same_len(matrix):
        is_a_valid_matrix = False
    elif not is_a_list_of_numerical_lists(matrix):
        is_a_valid_matrix = False
    return is_a_valid_matrix

def is_a_list_of_lists(matrix):
    is_a_valid_matrix = True
    for line in matrix:
        predicate = isinstance(line,list)
        if not predicate:
            is_a_valid_matrix = False
            break
    return is_a_valid_matrix

def is_a_list_of_numerical_lists(matrix):
    is_a_valid_matrix = True
    for line in matrix:
        if is_a_valid_matrix == False:
            break
        else:
            for element in line:
                predicate = isinstance(element,int)
                if not predicate:
                    is_a_valid_matrix = False
                    break
    return is_a_valid_matrix

def _process_matrix(matrix):
    #Crear lista de lista vacia para guardar la nueva matriz
    new_matrix = []
    #iterar por todos los elementos de la matriz (lista de listas).
    #Para acceder a cada elemento, usaremos dos índices (i y j), siendo que i representa la columna y j la fila. 
    for i, column in enumerate(matrix):
        new_list = []
        for j, value in enumerate(column):
            #print(f"[{i}][{j}]")
            new_value = process_element(i, j, matrix)
            #agregar a la nueva lista el avg calculado
            new_list.append(new_value)
            #agregar lista de valores a la nueva matriz
        new_matrix.append(new_list)
    return new_matrix

def all_lists_are_same_len(lista):
    same_len = True
    original_len = len(lista[0])
    for list in lista:
        if original_len != len(list):
            same_len = False
    return same_len

def process_element(i_index, j_index, elements):
    """
    Recibe el índice de un elemento y la lista en la que está,
    calcula su promedio con sus vecinos y devuelve dicho promedio
    """
    #obtengo la lista de vecinos representada por una lista de tuplas
    indices = get_neighbour_indices(i_index,j_index, elements)

    #obtengo valores de los vecinos
    values = get_neighbour_values(indices, elements)

    # calculo su promedio
    average = get_average(values)
 
    # devuelvo el valor final
    return average

def get_neighbour_indices(i_index,j_index, elements):
    """
    Devuelve la lista de índices tupla de los vecinos. Se incluye al
    propio elemento
    """
    #crear una lista vacia donde guardar las tuplas que representan las coordenadas en la matriz
    indices = []
    #agregar todos los vecinos posibles
    indices.append((i_index + 1, j_index + 1 ))
    indices.append((i_index + 1, j_index - 1 ))

    indices.append((i_index -1,j_index - 1))
    indices.append((i_index - 1, j_index + 1 ))

    indices.append((i_index, j_index + 1 ))
    indices.append((i_index, j_index - 1 ))

    indices.append((i_index -1,j_index))
    indices.append((i_index +1, j_index))
    

    #incluyo al propio elemento como vecino de sí mismo para facilitar el cálculo del avg después.
    indices.append((i_index,j_index))

    #elimino los indices imposibles (comprobar que coordenada[0] no sea menor que cero o mayores o igual 
    # a la longitud de la matriz, y comprobar que coordenada[1] no sea menor que cero o mayor o igual que la longitud 
    # de la lista en la que estamos) En una matriz todas las filas tienen la misma longitud, pero la longitud de una matriz 
    # puede ser menor que la longitud de la fila. 
    # x[0] representa el primer elemento de la tupla, y x[1] el segundo
    
    #filtar dependiendo de si es una matriz de una fila o no
    
    indices = my_filter(indices, lambda x: x[0]<0 or x[0]>= len(elements) or x[1]<0 or x[1]>= len(elements[0]))



    #devuelvo la lista filtrada
    #str_indices = ""
    #for coord in indices:
    #   str_indices += f"Indices [{coord[0]}]{coord[1]}]"
    #print(str_indices)
    return indices

def my_filter(elements, predicate):
    """
    recibe una lista y un predicado. Devuelve otra lista con aquellos elementos
    que superan el test del predicado
    """
    #gurdarmos copia de la lista de tuplas en otra lista 
    accum = elements.copy()

    #iteramos lista 
    for element in elements:
        #comprobar si la tupla tiene como elemento indices imposibles (menores que cero y mayores o igual 
        # a la longitud de la lista)
        if predicate(element):
            #si es así, elimino la tupla de la lista.
            accum.remove(element)
    #devuelvo la lista filtrada
    return accum


def get_neighbour_values (indices, elements):
    #La funcion recibe una lista de tuplas que representa la posicion del vecino en la matriz. Ej: tupla = (0,0) == elements[0][0]. 
    # elements representa la matriz 

    #crear una lista vacia donde guardar los valores de los vecinos
    values = []

    #iterar la lista de tuplas para conseguir el valor de la lista de los vecinos.
    for index in indices:
        values.append(elements[index[0]][index[1]])
    #    print(f"[{elements[index[0]][index[1]]}]")
    return values

def get_average(numbers):
    """"
    Recibe una lista de números (valores de los vecinos) y devuelve su promedio
    """
    return reduce(lambda accum, b: accum + b, numbers, 0) / len(numbers)

#def test():
    matriz1 = [[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]]
    matriz0 = []
    #matriz2 = [[4,3,2,1],[4,3,2,1],[4,3,2,1,5]]

    if process_matrix(matriz0)!= []:
        print("Test 0 failed")
    if process_matrix(matriz1) != [[3.5, 3.0, 2.0, 1.5],[3.5, 3.0, 2.0, 1.5],[3.5, 3.0, 2.0, 1.5],[3.5, 3.0, 2.0, 1.5]]:
        print(f"Test 1 failed")
    
  

process_matrix([[4,3,2,1],[4,3,2,1],[4,3,2,1],[4,3,2,1]])