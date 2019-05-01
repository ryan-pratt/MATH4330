def vandermonde(n, vector):
    result = [[0] * len(vector)] * n
    for i in range(n):
        col = [0] * len(vector)
        for j in range(len(vector)):
            col[j] = vector[j] ** i
        result[i] = col
    return result

def modified_gs(matrix):
    temp = [[0] * len(matrix[0])] * len(matrix)
    R = [[0] * len(matrix[0])] * len(matrix)
    Q = [[0] * len(matrix[0])] * len(matrix)
    for i in range(len(matrix)):
        temp[i] = matrix[i]
    for i in range(len(matrix)):
        R[i][i] = p_norm(2, temp[i])
        Q[i] = scalar_vector_mult(inverse(R[i][i]), temp[i])
        for j in range(i+1, len(matrix)):
            R[i][j] = dot_product(Q[i], temp[j])
            temp[j] = vector_subtract(temp[j], scalar_vector_mult(R[i][j], Q[i]))
    return [Q, R]

def p_norm(p, v):
    result = 0;
    for element in v:
        result += abs(element) ** p
    return result ** (1 / p)

def scalar_vector_mult(s, v):
    for element in v:
        element *= s
    return v

def vector_subtract(a, b):
    for i in range(len(a)):
        a[i] -= b[i]
    return a

def conjugate_transpose(matrix):
    return conjugate_matrix(transpose(matrix))

def back_substitution(R, b):
    result = b
    for i in range(len(b)-1, 1, -1):
        for j in range(i+1, len(b)):
            result[i] -= R[i][j] * result[j]
        result[i] *= inverse(R[i][i])
    return result

def inverse(s):
    return conjugate(s) / (s * conjugate(s))
    
def matrix_vector_mult(matrix, vector):
    result = [0] * len(vector)
    for i in range(len(matrix)):
        result[i] = dot_product(matrix[i], vector)
    return result

def dot_product(a, b):
    result = 0;
    for i in range(len(a)):
        result += conjugate(a[i]) * b[i]
    return result

def conjugate(s):
    return s.real - s.imag

def conjugate_matrix(matrix):
    for col in matrix:
        for element in col:
            element = conjugate(element)
    return matrix

def transpose(matrix):
    result = [[0] * len(matrix)] * len(matrix[0])
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix[j][i]
    return result
