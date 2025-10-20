"""
Taller 3.1 - Ejercicios de Probabilidad Conjunta
Distribuciones Bivariadas y Funciones de Densidad Conjunta
Autor: Contreras Yepes Juan Diego - 20211020069
Universidad Distrital Francisco José de Caldas
"""

from sympy import symbols, integrate, simplify, Rational, binomial, sqrt, pi
from sympy import N as numeric_eval

print("="*80)
print("TALLER 3.1 - EJERCICIOS DE PROBABILIDAD CONJUNTA")
print("="*80)

# ==============================================================================
# EJERCICIO 1: DISTRIBUCIÓN DE CAJAS DE CHOCOLATE
# ==============================================================================
print("\n" + "="*80)
print("EJERCICIO 1: DISTRIBUCIÓN DE CAJAS DE CHOCOLATE")
print("="*80)
print("Enunciado:")
print("Una fábrica de dulces distribuye cajas de chocolate, cuya función de")
print("densidad conjunta es dada por:")
print("f(x,y) = (2/5)(2x + 3y)  para 0 ≤ x ≤ 1, 0 ≤ y ≤ 1")
print("f(x,y) = 0               en otro caso")
print("\n" + "-"*80)

# Definir variables simbólicas
x, y = symbols('x y', real=True, positive=True)

# Definir función de densidad
f_xy = Rational(2, 5) * (2*x + 3*y)
print(f"Función de densidad: f(x,y) = {f_xy}")

# -----------------------------------------------------------------------------
# a) Verificar que f(x,y) es una función de densidad conjunta
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("a) Verificar que f(x,y) es una función de densidad conjunta")
print("-"*80)

# Paso 1: Verificar no negatividad
print("\nPaso 1: Verificar que f(x,y) ≥ 0")
print("Como x,y ∈ [0,1], entonces 2x + 3y ≥ 0")
print("Por lo tanto, (2/5)(2x + 3y) ≥ 0 en el dominio")
print("✓ La función es no negativa")

# Paso 2: Verificar que la integral doble es 1
print("\nPaso 2: Verificar que ∫∫ f(x,y) dx dy = 1")

# Integral respecto a x primero
integral_x = integrate(f_xy, (x, 0, 1))
print(f"∫[0,1] f(x,y) dx = {integral_x}")

# Integral respecto a y
integral_xy = integrate(integral_x, (y, 0, 1))
print(f"∫[0,1] ∫[0,1] f(x,y) dx dy = {integral_xy}")
print(f"Valor numérico: {float(integral_xy)}")

if integral_xy == 1:
    print("✓ La integral doble es igual a 1")
    print("✓ Por lo tanto, f(x,y) SÍ es una función de densidad conjunta válida")
else:
    print("✗ La integral doble NO es igual a 1")

# -----------------------------------------------------------------------------
# b) Calcular P(R) donde R = {(x,y) | 0 ≤ x ≤ 1/2, 0 ≤ y ≤ 1/2}
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("b) Calcular P(R) donde R = {(x,y) | 0 ≤ x ≤ 1/2, 0 ≤ y ≤ 1/2}")
print("-"*80)

# Calcular la probabilidad en la región R
P_R = integrate(integrate(f_xy, (x, 0, Rational(1,2))), (y, 0, Rational(1,2)))
print(f"P(R) = ∫[0,1/2] ∫[0,1/2] f(x,y) dx dy")
print(f"P(R) = {P_R}")
print(f"P(R) = {float(P_R):.6f}")
print(f"P(R) ≈ {float(P_R)*100:.2f}%")


# ==============================================================================
# EJERCICIO 2: FUNCIÓN DE PROBABILIDAD DISCRETA
# ==============================================================================
print("\n\n" + "="*80)
print("EJERCICIO 2: FUNCIÓN DE PROBABILIDAD DISCRETA")
print("="*80)
print("Enunciado:")
print("Dada la función de probabilidad f(x,y) = xy/36")
print("para las variables aleatorias X e Y discretas,")
print("donde x = 1,2,3 y y = 1,2,3")
print("\n" + "-"*80)

# Definir función de probabilidad discreta
def f(x_val, y_val):
    """Función de probabilidad conjunta discreta"""
    return Rational(x_val * y_val, 36)

# Crear tabla de probabilidades
print("\nTabla de probabilidades conjuntas:")
print("-"*80)
print(f"{'x\\y':<8}", end="")
for j in [1, 2, 3]:
    print(f"{'y='+str(j):<12}", end="")
print()
print("-"*80)

for i in [1, 2, 3]:
    print(f"x={i:<6}", end="")
    for j in [1, 2, 3]:
        prob = f(i, j)
        print(f"{str(prob):<8} ({float(prob):.4f})  ", end="")
    print()
print("-"*80)

# Verificar que suma 1
suma_total = sum(f(i, j) for i in [1,2,3] for j in [1,2,3])
print(f"\nSuma total de probabilidades: {suma_total} = {float(suma_total)}")

# -----------------------------------------------------------------------------
# a) P(X + Y = 4)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("a) Calcular P(X + Y = 4)")
print("-"*80)
print("Pares donde x + y = 4: (1,3), (2,2), (3,1)")

pares_a = [(1,3), (2,2), (3,1)]
P_a = sum(f(i, j) for i, j in pares_a)

print(f"P(X+Y=4) = f(1,3) + f(2,2) + f(3,1)")
for i, j in pares_a:
    print(f"  f({i},{j}) = {f(i,j)} = {float(f(i,j)):.4f}")
print(f"P(X+Y=4) = {P_a} = {float(P_a):.4f}")
print(f"P(X+Y=4) ≈ {float(P_a)*100:.2f}%")

# -----------------------------------------------------------------------------
# b) P(X > Y)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("b) Calcular P(X > Y)")
print("-"*80)
print("Pares donde x > y: (2,1), (3,1), (3,2)")

pares_b = [(2,1), (3,1), (3,2)]
P_b = sum(f(i, j) for i, j in pares_b)

print(f"P(X>Y) = f(2,1) + f(3,1) + f(3,2)")
for i, j in pares_b:
    print(f"  f({i},{j}) = {f(i,j)} = {float(f(i,j)):.4f}")
print(f"P(X>Y) = {P_b} = {float(P_b):.4f}")
print(f"P(X>Y) ≈ {float(P_b)*100:.2f}%")

# -----------------------------------------------------------------------------
# c) P(X=2 ∪ Y≤1)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("c) Calcular P(X=2 ∪ Y≤1)")
print("-"*80)
print("Pares donde x=2 O y≤1: (2,1), (2,2), (2,3), (1,1), (3,1)")
print("Aplicando unión: (1,1), (2,1), (2,2), (2,3), (3,1)")

pares_c = [(1,1), (2,1), (2,2), (2,3), (3,1)]
P_c = sum(f(i, j) for i, j in pares_c)

print(f"P(X=2 ∪ Y≤1) = f(1,1) + f(2,1) + f(2,2) + f(2,3) + f(3,1)")
for i, j in pares_c:
    print(f"  f({i},{j}) = {f(i,j)} = {float(f(i,j)):.4f}")
print(f"P(X=2 ∪ Y≤1) = {P_c} = {float(P_c):.4f}")
print(f"P(X=2 ∪ Y≤1) ≈ {float(P_c)*100:.2f}%")

# -----------------------------------------------------------------------------
# d) P(X=2 ∪ Y=1)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("d) Calcular P(X=2 ∪ Y=1)")
print("-"*80)
print("Pares donde x=2 O y=1: (1,1), (2,1), (2,2), (2,3), (3,1)")
print("Nota: Esta es la misma unión que el inciso anterior")

# Alternativamente, si se interpreta como intersección:
print("\nSi se interpreta como intersección P(X=2 ∩ Y=1):")
P_d_interseccion = f(2, 1)
print(f"P(X=2 ∩ Y=1) = f(2,1) = {P_d_interseccion} = {float(P_d_interseccion):.4f}")

# Como unión (interpretación más común):
P_d = P_c  # Es la misma que el inciso c
print(f"\nComo unión: P(X=2 ∪ Y=1) = {P_d} = {float(P_d):.4f}")


# ==============================================================================
# EJERCICIO 3: SELECCIÓN DE ESTUDIANTES (HIPERGEOMÉTRICA)
# ==============================================================================
print("\n\n" + "="*80)
print("EJERCICIO 3: SELECCIÓN DE ESTUDIANTES")
print("="*80)
print("Enunciado:")
print("Se seleccionaron al azar 2 estudiantes de un salón que contiene:")
print("  - 3 estudiantes de Sistemas")
print("  - 2 estudiantes de Electrónica")
print("  - 3 estudiantes de Industrial")
print("Sea X = número de estudiantes de Sistemas")
print("Sea Y = número de estudiantes de Electrónica")
print("\n" + "-"*80)

# Parámetros del problema
n_sistemas = 3
n_electronica = 2
n_industrial = 3
total_estudiantes = n_sistemas + n_electronica + n_industrial
seleccionados = 2

print(f"Total de estudiantes: {total_estudiantes}")
print(f"Estudiantes seleccionados: {seleccionados}")

# -----------------------------------------------------------------------------
# 1. Función de probabilidad conjunta
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("1. Función de probabilidad conjunta")
print("-"*80)

# Total de formas de escoger 2 estudiantes de 8
N = binomial(total_estudiantes, seleccionados)
print(f"Total de formas de escoger {seleccionados} de {total_estudiantes}: C({total_estudiantes},{seleccionados}) = {N}")

# Función de probabilidad hipergeométrica bivariada
def f_hipergeom(x_val, y_val):
    """
    Función de probabilidad conjunta hipergeométrica
    x_val: número de estudiantes de sistemas
    y_val: número de estudiantes de electrónica
    """
    if x_val + y_val > seleccionados or x_val > n_sistemas or y_val > n_electronica:
        return 0
    
    z_val = seleccionados - x_val - y_val  # estudiantes de industrial
    
    if z_val < 0 or z_val > n_industrial:
        return 0
    
    numerador = binomial(n_sistemas, x_val) * binomial(n_electronica, y_val) * binomial(n_industrial, z_val)
    return Rational(numerador, N)

# Generar tabla de probabilidades
print("\nTabla de probabilidades f(x,y):")
print("-"*80)
print(f"{'(x,y)':<12} {'Cálculo':<35} {'Probabilidad':<15} {'Decimal'}")
print("-"*80)

probabilidades = {}
for x_val in range(min(n_sistemas, seleccionados) + 1):
    for y_val in range(min(n_electronica, seleccionados) + 1):
        if x_val + y_val <= seleccionados:
            z_val = seleccionados - x_val - y_val
            if z_val <= n_industrial:
                prob = f_hipergeom(x_val, y_val)
                if prob > 0:
                    probabilidades[(x_val, y_val)] = prob
                    calculo = f"C({n_sistemas},{x_val})·C({n_electronica},{y_val})·C({n_industrial},{z_val})/{N}"
                    print(f"f({x_val},{y_val}){'':<6} {calculo:<35} {prob:<15} {float(prob):.4f}")

print("-"*80)

# Verificar que suma 1
suma_prob = sum(probabilidades.values())
print(f"Suma de probabilidades: {suma_prob} = {float(suma_prob)}")

# -----------------------------------------------------------------------------
# 2. Calcular P(X + Y = 1)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("2. Calcular P(X + Y = 1)")
print("-"*80)
print("Esto significa que se seleccionó exactamente 1 estudiante de sistemas")
print("o electrónica, y el otro es de industrial")
print("Pares posibles: (0,1) y (1,0)")

P_sum1 = f_hipergeom(0, 1) + f_hipergeom(1, 0)
print(f"\nP(X+Y=1) = f(0,1) + f(1,0)")
print(f"         = {f_hipergeom(0,1)} + {f_hipergeom(1,0)}")
print(f"         = {P_sum1}")
print(f"         = {float(P_sum1):.6f}")
print(f"         ≈ {float(P_sum1)*100:.2f}%")


# ==============================================================================
# RESUMEN DE RESULTADOS
# ==============================================================================
print("\n\n" + "="*80)
print("RESUMEN DE RESULTADOS")
print("="*80)

print("\nEJERCICIO 1: DISTRIBUCIÓN DE CAJAS DE CHOCOLATE")
print(f"  - f(x,y) es una función de densidad conjunta válida: ✓")
print(f"  - P(R) en región [0,1/2]×[0,1/2] = {P_R} ≈ {float(P_R)*100:.2f}%")

print("\nEJERCICIO 2: FUNCIÓN DE PROBABILIDAD DISCRETA")
print(f"  a) P(X+Y=4)     = {P_a} ≈ {float(P_a)*100:.2f}%")
print(f"  b) P(X>Y)       = {P_b} ≈ {float(P_b)*100:.2f}%")
print(f"  c) P(X=2 ∪ Y≤1) = {P_c} ≈ {float(P_c)*100:.2f}%")
print(f"  d) P(X=2 ∩ Y=1) = {P_d_interseccion} ≈ {float(P_d_interseccion)*100:.2f}%")

print("\nEJERCICIO 3: SELECCIÓN DE ESTUDIANTES")
print(f"  - Total de combinaciones posibles: {N}")
print(f"  - Casos válidos en la distribución: {len(probabilidades)}")
print(f"  - P(X+Y=1) = {P_sum1} ≈ {float(P_sum1)*100:.2f}%")

print("\n" + "="*80)
print("FIN DEL TALLER 3.1")
print("="*80)
