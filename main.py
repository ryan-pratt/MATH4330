import algorithms.py as algs

def degree_4_interpolation(features, labels):
    A = algs.vandermonde(4, features)
    gs = algs.modified_gs(A)
    Q = gs[0]
    R = gs[1]
    Q_star = algs.conjugate_transpose(Q)
    alpha = algs.back_substitution(R, algs.matrix_vector_mult(Q_star, labels))
    print(f'p(x) = {alpha[0]} + {alpha[1]}x + {alpha[2]}x^2 + {alpha[3]}x^3')
