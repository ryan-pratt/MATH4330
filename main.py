import algorithms as algs

def degree_4_interpolation(features, labels):
    """ Finds the coefficients for the degree 4 polynomial that best fits the 
        given input

    This finds the coefficients for the degree 4 polynomial, 
    p(x) = a + bx + cx^2 + dx^3, by building the degree 4 Vandermonde matrix 
    for the given features, performing the modified (stable) Gram-Schmidt 
    algorithm on that Vandermonde matrix to obtain it's QR factorization, then 
    performs back-substitution on Q* and the given labels to obtain a vector 
    containing the coefficient values for the polynomial.

    Args:
        features (array of complex numbers): the features of the polynomial
        labels (array of complex numbers): the labels of the polynomial

    Returns:
        array of complex numbers: the vector containing the coefficients of the
            polynomial, [a,b,c,d]

    """
    A = algs.vandermonde(4, features)
    gs = algs.modified_gs(A)
    Q = gs[0]
    R = gs[1]
    Q_star = algs.conjugate_transpose(Q)
    alpha = algs.back_substitution(R, algs.matrix_vector_mult(Q_star, labels))
    return alpha

#this is a test with random input and prints the output formatted into a string
if __name__ == "__main__":
    f = [0+0j, -0.69583+0j, 1+0j, 2+0j]
    l = [1+0j, 0+0j, 10+0j, 49+0j]
    alpha = degree_4_interpolation(f, l)
    print("p(x) = {0} + {1}x + {2}x^2 + {3}x^3".format(alpha[0], alpha[1], alpha[2], alpha[3]))

