def vandermonde(n, vector):
    """ Finds the degree n Vandermonde matrix for the given vector

    This initializes a new matrix of the dimensions of the output matrix, then
    iterates over each element in each column and calculates its value with
    vector[element] ** column_number

    Args:
        n (integer): the degree of the Vandermonde matrix to build (the number
            of columns)
        vector (array of complex numbers): the vector to build the Vandermonde
            matrix for

    Returns:
        array of arrays of complex numbers: the Vandermonde matrix as a list of
            column vectors

    """

    result = gen_matrix(n,len(vector))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = vector[j] ** i
    return result


def modified_gs(matrix):
    """ Finds the QR factorization of the given matrix using the modified
    (stable) Gram-Schmidt algorithm

    This uses a temporary matrix to build up the matrices Q and R. It first
    initializes the temporary matrix with the columns of the input matrix. It
    then iterates over each column to build up Q and R.

    Args:
        matrix (array of arrays of complex numbers): the matrix to perform QR
            factorization on as a list of column vectors

    Returns:
        array: a two element array where the element at index 0 is Q and the
            element at index 1 is R, where Q and R are matrices as lists of
            column vectors (arrays of arrays of complex numbers) such that Q is
            unitary, R is upper-triangular, and QR = the input matrix

    """

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
    """ Finds the p-norm of a vector

    This finds the p-norm of a vector by summing each element of the vector
    raised to the power of p, then raising that sum to the power of 1/p.

    Args:
        p (integer): the p-norm to find
        v (array of complex numbers): the vector to find the p-norm of

    Returns:
        complex number: the result of the p-norm of v

    """

    result = 0;
    for element in v:
        result += abs(element) ** p
    return result ** (1 / p)


def scalar_vector_mult(s, v):
    """ Multiplies a vector by a scalar

    This multiplies a vector by a scalar by multiplying each element of the
    vector by the scalar.

    Args:
        s (complex number): the scalar
        v (array of complex numbers): the vector

    Returns:
        array of complex numbers: sv

    """

    result = gen_vector(len(v)) 
    for i in range(len(v)):
        result[i] = s * v[i]
    return result


def vector_subtract(a, b):
    """ Subtracts two vectors

    This subtracts a vector from another vector by iterating through each
    element of the two vectors

    Args:
        a (array of complex numbers): the first vector
        b (array of complex numbers): the vector to subtract from the first
            vector

    Returns:
        array of complex numbers: the difference between a and b

    """

    result = gen_vector(len(a)) 
    for i in range(len(a)):
        result[i] = a[i] - b[i]
    return result


def conjugate_transpose(matrix):
    """ Computes the conjugate transpose of a matrix

    This computes the conjugate transpose of a matrix by first transposing the
    matrix and then taking the conjugate of that result

    Args:
        matrix (array of arrays of complex numbers): the matrix

    Returns:
        array of arrays of complex numbers: the conjugate transpose of the input
            matrix

    """

    return conjugate_matrix(transpose(matrix))


def back_substitution(R, b):
    """ Performs back substitution on the input matrix and vector

    This performs back substitution on a matrix with a given vector by iterating
    bottom-up through each element of the input matrix

    Args:
        R (array of arrays of complex numbers): the upper-triangular matrix as a
            list of column vectors
        b (array of complex numbers): the matrix

    Returns:
        array of complex numbers: the resulting values from the
            back-substitution

    """

    result = b
    for i in range(len(b)-1, 1, -1):
        for j in range(i+1, len(b)):
            result[i] -= R[i][j] * result[j]
        result[i] *= inverse(R[i][i])
    return result


def inverse(s):
    """ Finds the multiplicative inverse of a complex number

    This finds the multiplicative inverse by dividing the conjugate of the input
    number into the number multiplied by its conjugate.

    Args:
        s (complex number): the input scalar

    Returns:
        complex number: the multiplicative inverse of the input

    """

    return conjugate(s) / (s * conjugate(s))
    

def matrix_vector_mult(matrix, vector):
    """ Multiplies a matrix by a vector of compatible dimensions

    This computes the multiplication of a matrix by a vector by computing the
    dot product of the vector and each column of the matrix.

    Args:
        matrix (array of arrays of complex numbers): the matrix as a list of
            column vectors
        vector (array of complex numbers): the vector to multiply the matrix by

    Returns:
        array of complex numbers: the resulting vector from the matrix
            multiplication

    """

    result = gen_vector(len(vector))
    for i in range(len(matrix)):
        result[i] = dot_product(matrix[i], vector)
    return result


def dot_product(a, b):
    """ Computes the dot product of two complex vectors of equal dimensions

    This computes the dot product of two vectors by summing the product of each
    element of the conjugate of the first vector times the corresponding element
    of the second vector.

    Args:
        a (array of complex numbers): the first vector
        b (array of complex numbers): the second vector

    Returns:
        complex number: a.b

    """

    result = 0;
    for i in range(len(a)):
        result += conjugate(a[i]) * b[i]
    return result


def conjugate(s):
    """ Computes the complex conjugate of a complex number

    This takes a complex number and returns its complex conjugate by subtracting
    the imaginary part from the real part.

    Args:
        s (complex number): the scalar to conjugate

    Returns:
        complex number: the conjugate of s

    """

    result = s.real
    result -= (s.imag)*1j
    return result


def conjugate_matrix(matrix):
    """ Computes the complex conjugate of a matrix

    This computes the complex conjugate of a matrix by conjugating each element
    in the matrix

    Args:
        matrix (array of arrays of complex numbers): the matrix to conjugate

    Returns:
        array of arrays of complex numbers: the conjugate of the matrix

    """

    result = gen_matrix(len(matrix),len(matrix[0]))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = conjugate(matrix[i][j])
    return result


def transpose(matrix):
    """ Computes the transpose of a matrix

    This computes the transpose of a matrix by swapping the elements across the
    diagonal.

    Args:
        matrix (array of arrays of elements): the matrix to transpose

    Returns:
        array of arrays of elements: the transpose of the matrix

    """

    result = gen_matrix(len(matrix[0]),len(matrix))
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix[j][i]
    return result


def gen_vector(n):
    """ This generates a new vector of a given length containing all 0's

    This iterates n times to append 0's to the end of a new, empty array

    Args:
        n (integer): the length of the desired vector

    Returns:
        array of complex numbers: the new, initialized vector

    """

    v = []
    for i in range(n):
        v.append(0+0j)
    return v


def gen_matrix(m,n):
    """ This generates a new matrix of the given dimensions

    This iterates through m to append new vectors of length n to the matrix.

    Args:
        m (integer): the number of columns
        n (integer): the number of rows

    Returns:
        array of arrays of complex numbers: the new, initialized matrix as a
            list of column vectors

    """

    matrix = []
    for i in range(m):
        matrix.append(gen_vector(n))
    return matrix
