def vandermonde(n, vector):
    result = gen_matrix(n,len(vector))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = vector[j] ** i
    return result

def modified_gs(matrix):
    v = gen_matrix(len(matrix),len(matrix[0]))
    R = gen_matrix(len(matrix),len(matrix[0]))
    Q = gen_matrix(len(matrix),len(matrix[0]))
    for i in range(len(matrix)):
        v[i] = matrix[i]
    for i in range(len(matrix)):
        R[i][i] = p_norm(2, v[i])
        Q[i] = scalar_vector_mult(inverse(R[i][i]), v[i])
        for j in range(i+1, len(matrix[0])):
            R[j][i] = dot_product(Q[i], v[j])
            v[j] = vector_subtract(v[j], scalar_vector_mult(R[j][i], Q[i]))
    return [Q, R]

def p_norm(p, v):
    result = 0;
    for element in v:
        result += abs(element) ** p
    return result ** (1 / p)

def scalar_vector_mult(s, v):
    result = gen_vector(len(v)) 
    for i in range(len(v)):
        result[i] = s * v[i]
    return result

def vector_subtract(a, b):
    result = gen_vector(len(a)) 
    for i in range(len(a)):
        result[i] = a[i] - b[i]
    return result

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
    result = gen_vector(len(vector))
    for i in range(len(matrix)):
        result[i] = dot_product(matrix[i], vector)
    return result

def dot_product(a, b):
    result = 0;
    for i in range(len(a)):
        result += conjugate(a[i]) * b[i]
    return result

def conjugate(s):
    #I can't figure out how to make this work
    #result = s.real
    #result -= (s.imag)j    <-- it doesn't like the (...)j
    return s.conjugate()

def conjugate_matrix(matrix):
    result = gen_matrix(len(matrix),len(matrix[0]))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = conjugate(matrix[i][j])
    return result

def transpose(matrix):
    result = gen_matrix(len(matrix[0]),len(matrix))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix[j][i]
    return result

def gen_vector(n):
    v = []
    for i in range(n):
        v.append(0)
    return v

def gen_matrix(m,n):
    matrix = []
    for i in range(m):
        matrix.append(gen_vector(n))
    return matrix
