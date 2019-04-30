def vandermonde(n, vector):
    result = [[0] * len(vector)] * n
    for i in range(n-1):
        col = []
        for j in range(1, m):
            col[j] = vector[j] ** i
        result[i+1] = col
    return result

def modified_gs(matrix):
    #TODO

def conjugate_transpose(matrix):
    return conjugate_matrix(transpose(matrix))

def back_substitution(R, b):
    result = b
    for i in range(n, 1, -1):
        for j in range(i+1, n):
            result[i] -= R[i][j] * result[j]
        result[i] *= inverse(R[i][i])
    return result

def inverse(s):
    return conjugate(s) / (s * conjugate(s))
    
def matrix_vector_mult(matrix, vector):
    result = [0] * len(vector)
    for i in range(len(matrix)):
        result[i] = vector_dot_product(matrix[i], vector)
    return result

def vector_dot_product(a, b):
    result = 0;
    for i in range(n):
        result += conjugate(a[i]) * b[i]
    return result

def conjugate(s):
    return s.real - s.imaj

def conjugate_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = conjugate(matrix[i][j])
    return matrix

def transpose(matrix):
    result = [[0] * len(matrix)] * len(matrix[0])
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix[j][i]
    return result
