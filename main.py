import algorithms.py as algs

if __name__ == "__main__":
    x = some vector
    y = some vector

    A = algs.vandermonde(4, x)
    gs = algs.modified_gs(A)
    Q = gs[0]
    R = gs[1]
    Q_star = algs.conjugate_transpose(Q)
    alpha = algs.back_substitution(R, algs.matrix_vector_mult(Q_star, y))
    print(f'p(x) = {alpha[0]} + {alpha[1]}x + {alpha[2]}x^2 + {alpha[3]}x^3')
