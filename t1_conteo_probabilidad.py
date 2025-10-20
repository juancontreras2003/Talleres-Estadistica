"""
T1 – Seis ejercicios de conteo y probabilidad según enunciados

Autor: Contreras Yepes Juan Diego – 20211020069
Universidad Distrital Francisco José de Caldas
"""

from math import comb, factorial
from collections import Counter
from fractions import Fraction

# Ejercicio 1: Selección de 3 estudiantes
n_sis, n_ele, n_ind = 3, 2, 3
total_est = n_sis + n_ele + n_ind
total_combos = comb(total_est, 3)

# a) P(3 de Electrónica)
p_3E = comb(n_ele, 3) / total_combos
# b) P(3 de Sistemas)
p_3S = comb(n_sis, 3) / total_combos
# c) P(ninguno de Industrial)
p_noI = comb(n_sis + n_ele, 3) / total_combos
# d) P(1 de cada carrera)
p_1c = (comb(n_sis,1) * comb(n_ele,1) * comb(n_ind,1)) / total_combos

# Ejercicio 2: Permutaciones y combinaciones (n=8, k=3)
n, k = 8, 3
perm_no_rep = factorial(n) // factorial(n - k)  # P(n,k) sin repetición
perm_con_rep = n ** k                           # P(n,k) con repetición
comb_no_rep = comb(n, k)                       # C(n,k) sin repetición
comb_con_rep = comb(n + k - 1, k)               # C(n,k) con repetición

# Ejercicio 3: Uno de cada carrera (alias del 1.d)
p_1c_alias = p_1c

# Ejercicio 4: Arreglo de libros por asignatura (4,6,2)
a_ing, a_ingl, a_fis = 4, 6, 2
total_libros = a_ing + a_ingl + a_fis
arr_todos = factorial(total_libros)  # total de arreglos
esspo = 3  # bloques: Ing/Ingl/Fis
arr_bloques = factorial(esspo) * factorial(a_ing) * factorial(a_ingl) * factorial(a_fis)

# Ejercicio 5: Dos lanzamientos de un par de dados
pmf_suma = Counter(i + j for i in range(1,7) for j in range(1,7))

def p_no_suma(target):
    """
    Probabilidad de NO obtener la suma 'target' en ambos lanzamientos.
    """
    p = Fraction(pmf_suma[target], 36)
    return (1 - p) ** 2

# Ejercicio 6: Distribución binomial

def binom_pmf(n, p, k):
    """P(X=k) = C(n,k) p^k (1-p)^(n-k)"""
    return Fraction(comb(n, k), 1) * Fraction(p**k) * Fraction((1-p)**(n-k))

def binom_cdf_ge(n, p, k):
    """P(X>=k) = sum_{j=k..n} P(X=j)"""
    return sum(binom_pmf(n, p, j) for j in range(k, n+1))

def binom_range(n, p, a, b):
    """P(a<=X<=b) = sum_{j=a..b} P(X=j)"""
    return sum(binom_pmf(n, p, j) for j in range(a, b+1))

# Imprimir resultados
print("Ejercicio 1:")
print(" P(3 Electrónica)   =", p_3E)
print(" P(3 Sistemas)      =", p_3S)
print(" P(ninguno Industrial) =", p_noI)
print(" P(1 de cada carrera)  =", p_1c)

print("\nEjercicio 2:")
print(" P(n,k) sin rép =", perm_no_rep)
print(" P(n,k) c/ rép =", perm_con_rep)
print(" C(n,k) sin rép =", comb_no_rep)
print(" C(n,k) c/ rép =", comb_con_rep)

print("\nEjercicio 3:")
print(" P(1 de cada carrera) =", p_1c_alias)

print("\nEjercicio 4:")
print(" Total arreglos      =", arr_todos)
print(" Arreglos en bloques =", arr_bloques)

print("\nEjercicio 5:")
for target in (7, 11):
    print(f" P(no suma {target} en ambos) =", p_no_suma(target))

print("\nEjercicio 6 (ejemplo n=10,p=0.3,k=2,a=1,b=3):")
print(" P(X=k)   =", binom_pmf(10, 0.3, 2))
print(" P(X>=k)  =", binom_cdf_ge(10, 0.3, 2))
print(" P(1<=X<=3)=", binom_range(10, 0.3, 1, 3))
