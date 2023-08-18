import numpy as np

# item 1
def soma_vetor(vetor_1, vetor_2)
    soma = vetor_1 + vetor_2
    return soma

#item 3

ndarray_4 = np.array([[1,2,3,4],[1,2,3,4]])
#multilpicando 
ndarray_4 = ndarray_4 * ndarray_3 

# item 6

A= np.array ([1,2,3])
B= np.array ([4,5,6])

produto_vetorial = np.cross(A,B)
#produto vetorial A x B
print(produto_vetorial)


# item 2

def reshape_and_float (vector_1)
    
    a1d_3_reshaped = np.reshape(a1d_3, (2,2))
    a1d_3_reshaped = np.array([a1d_3_reshaped], dtype='float32'
                              
# item 5

def item_5 (vector_1, vector_2)
    empilhado = np.hstack((vector1, vector2))
    print np.mean(empilhado)
    print np.std(empilhado)
    print np.var(empilhado)

    indices_pares = (empilhado%2 == 0)
                                  
# item 7

def matrix_info (a1d)
    identidade = np.eye(a1d)
    determinante = np.linalg.det(a1d)
    inversa = np.linalg.inv(a1d)
    print ("\n\nIdentidade: ", identidade, "\nDeterminante: ", determinante, "\nInversa: ", inversa, "Corretude: \n\n")

