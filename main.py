import algorithms as algs

def degree_4_interpolation(features, labels):
    A = algs.vandermonde(4, features)
    gs = algs.modified_gs(A)
    Q = gs[0]
    R = gs[1]
    Q_star = algs.conjugate_transpose(Q)
    alpha = algs.back_substitution(R, algs.matrix_vector_mult(Q_star, labels))
    print("p(x) = {0} + {1}x + {2}x^2 + {3}x^3".format(alpha[0], alpha[1], alpha[2], alpha[3]))

if __name__ == "__main__":
    f = [0+0j, -0.69583+0j, 1+0j, 2+0j]
    l = [1+0j, 0+0j, 10+0j, 49+0j]
    degree_4_interpolation(f, l)
