def negate_vector(vector):
    """Negates all elements in a vector

    This negates a vector by negating all the elements in it

    Args:
        vector (list): the vector to be negated

    Returns:
        list: the negated vector

    """

    for element in vector:
        element = 0 - element
    return vector


def add_vectors(vector_a, vector_b):
    """Adds two vectors of equal dimensions

    This takes two vectors, as lists, of equal length, computes their sum,
    and returns that sum as a list.

    Args:
        vector_a (list): first vector
        vector_b (list): second vector

    Returns:
        list: vector_a + vector_b

    """
    
    for i in range(len(vector_a)):
        vector_a[i] += vector_b[i]
    return vector_a


def subtract_vectors(vector_a, vector_b):
    """Subtracts two vectors of equal dimensions

    This takes two vectors, as lists, of equal length, computes their
    difference, and returns that difference as a list by adding the negation 
    of vector_b to vector_a.

    Args:
        vector_a (list): first vector
        vector_b (list): the vector to be subtracted

    Returns:
        list: vector_a - vector_b

    """

    return add_vectors(vector_a, negate_vector(vector_b))


def conjugate_number(complex_number):
    """Computes the conjugate of a complex number

    This takes a complex number and returns its complex conjugate by
    changing the sign of the imaginary part.

    Args:
        complex_number (number): complex number

    Returns:
        number: the conjugate of number

    """

    result = complex_number.real
    result -= complex_number.imag * 1j
    return result


def conjugate_matrix(matrix):
    """Computes the conjugate of a matrix

    This computes the complex conjugate of a matrix, as a list of columns,
    by taking the conjugate of each element of the matrix

    Args:
        matrix (list of lists): matrix as list of columns

    Returns:
        list of lists: conjugate of matrix
    
    """

    for column in matrix:
        for element in column:
            element = conjugate_number(element)
    return matrix


def orthogonal_decomposition(orthonormal_set, vector):
    """Computes an orthogonal vector

    This computes the orthogonal decomposition of a vector with respect 
    to orthonormal_set

    Args:
        orthonormal_set (list of lists): orthonormal list of vectors
        vector (list): a vector of compatible dimension to the vectors 
        in orthonormal_set

    Returns:
        list: a vector that is orthogonal to the vectors in orthonormal_set

    """

    result = [0 for n in range(len(vector))]
    for i in range(len(orthonormal_set) - 1):
        dotProduct = vector_dot_product(orthonormal_set[i], vector)
        newVector = multiply_scalar_vector(dotProduct, orthonormal_set[i])
        result = add_vectors(result, newVector)
    return subtract_vectors(vector, result)


def multiply_scalar_vector(scalar, vector):
    """Multiplies a vector by a scalar

    This multiplies a vector by a scalar by multiplying each element of
    the vector by the scalar

    Args:
        scalar (number): scalar
        vector (list): vector

    Returns:
        list: scalar * vector

    """

    for element in vector:
        element *= scalar
    return vector


def multiply_scalar_matrix(scalar, matrix):
    """Multiplies a matrix by a scalar

    This computes the multiplication of a scalar by a matrix by computing
    the scalar vector multiplication for each column in the matrix.

    Args:
        scalar (number): scalar
        matrix (list of lists): matrix as list of columns

    Returns:
        list of lists: scalar * matrix

    """

    for column in matrix:
        column = multiply_scalar_vector(scalar, column)
    return matrix


def multiply_matrix_vector(matrix, vector):
    """Multiplies a matrix by a vector of compatible dimensions

    This computes the multiplication of a matrix by a vector by computing the
    dot product of the vector and each column of the matrix.

    Args:
        matrix: (list of lists): matrix as list of columns
        vector (list): vector

    Returns:
        list: matrix * vector

    """

    result = [0] * len(vector)
    for i in range(len(matrix)):
        result[i] = vector_dot_product(vector, matrix[i])
    return result


def multiply_matrices(matrix_a, matrix_b):
    """Multiplies two matrices of compatible dimensions

    This computes the multiplication of two matrices by computing the 
    dot product of each column of the first matrix with each column of 
    the second matric.

    Args:
        matrix_a (list of lists): first matrix as list of columns
        matrix_b (list of lists): second matrix as list of columns

    Returns:
        list of lists: matrix_a * matrix_b

    """

    result = [[0] * len(matrix_b[0])] * len(matrix_a)
    matrix_a = transpose(matrix_a)
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = vector_dot_product(matrix_a[i], matrix_b[j])
    return result


def vector_dot_product(vector_a, vector_b):
    """Computes the dot product of two vectors of equal dimensions

    This computes the dot product of two vectors by summing
    the product of each element of the vectors.

    Args:
        vector_a (list): first vector
        vector_b (list): second vector

    Returns:
        number: vector_a * vector_b

    """

    result = 0
    for i in range(len(vector_a)):
        result += vector_a[i] * vector_b[i]

    return result


def transpose(matrix):
    """Computes the transpose of a matrix

    This computes the transpose of a matrix by swapping
    the elements across the diagonal.

    Args:
        matrix (list of lists): matrix as list of columns

    Returns:
        list of lists: Transpose of matrix

    """

    result = [[0] * len(matrix)] * len(matrix[0])
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = matrix[j][i]
    return result


def conjugate_transpose(matrix):
    """Computes the conjugate transpose of a matrix

    This computes the conjugate transpose of a matrix by first transposing
    a matrix and then taking the conjugate of that result.

    Args:
        matrix (list of lists): matrix as list of columns

    Returns:
        list of lists: Transpose of matrix

    """

    return conjugate_matrix(transpose(matrix))


def p_norm(p, vector):
    """Computes the p-norm of a vectrix

    This computes the p-norm of a vector by summing the absolute value
    of each element in the vector raised to p, and then raising the
    result to 1/p

    Args:
        p (integer): p
        vector (list): vector

    Returns:
        number: ||vector||_p
    
    """

    result = 0
    for element in vector:
        result += (abs(element)) ** p
    return result ** (1/p)


if __name__ == "__main__":
    # test_a = [1+2j, 3+4j]
    # test_b = [0, 6]
    test_a = [1,0,2]
    test_b = [0,1,1]
    test_c = [1,0,0]
    print(orthogonal_decomposition([test_a, test_b], test_c))
