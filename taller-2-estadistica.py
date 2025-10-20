"""
Taller 2 - Ejercicios de Estadística
Funciones de Probabilidad y Distribuciones
Autor: Contreras Yepes Juan Diego - 20211020069
Universidad Distrital Francisco José de Caldas
"""

from sympy import symbols, integrate, Rational, sqrt, simplify
from sympy import N as numeric_eval
import matplotlib.pyplot as plt
import numpy as np

print("="*80)
print("TALLER 2 - EJERCICIOS DE ESTADÍSTICA")
print("="*80)

# ==============================================================================
# EJERCICIO 1: FUNCIÓN DE DENSIDAD CONTINUA
# ==============================================================================
print("\n" + "="*80)
print("EJERCICIO 1: FUNCIÓN DE DENSIDAD CONTINUA")
print("="*80)
print("Enunciado:")
print("Dada la función f(x) = kx² para 0 ≤ x ≤ 6")
print("Hallar k y calcular P(1 ≤ x ≤ 2.5)")
print("\n" + "-"*80)

# Definir variable simbólica
x = symbols('x', real=True, positive=True)

# -----------------------------------------------------------------------------
# Paso 1: Encontrar el valor de k
# -----------------------------------------------------------------------------
print("\nPaso 1: Encontrar el valor de k")
print("-"*80)
print("Para que f(x) sea una función de densidad, debe cumplir:")
print("∫[0,6] kx² dx = 1")

# Calcular la integral
k = symbols('k', positive=True)
f_x = k * x**2
integral = integrate(f_x, (x, 0, 6))
print(f"\n∫[0,6] kx² dx = {integral}")

# Resolver para k
k_value = 1 / integral.subs(k, 1)
print(f"\n{integral} = 1")
print(f"k = 1/{integral.subs(k, 1)}")
print(f"k = {k_value}")
print(f"k = {float(k_value):.6f}")

# -----------------------------------------------------------------------------
# Paso 2: Función de probabilidad
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 2: Función de probabilidad")
print("-"*80)

f_x_final = k_value * x**2
print(f"f(x) = {f_x_final}  para 0 ≤ x ≤ 6")
print(f"f(x) = 0           en otro caso")

# -----------------------------------------------------------------------------
# Paso 3: Función acumulativa F(x)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 3: Función acumulativa F(x)")
print("-"*80)

# Calcular F(x) = ∫[0,x] f(t) dt
t = symbols('t', real=True, positive=True)
F_x = integrate(k_value * t**2, (t, 0, x))
F_x_simplified = simplify(F_x)
print(f"F(x) = ∫[0,x] f(t) dt")
print(f"F(x) = {F_x_simplified}  para 0 ≤ x ≤ 6")
print(f"F(x) = 0                 para x < 0")
print(f"F(x) = 1                 para x > 6")

# -----------------------------------------------------------------------------
# Paso 4: Calcular P(1 ≤ x ≤ 2.5)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 4: Calcular P(1 ≤ x ≤ 2.5)")
print("-"*80)

# Método 1: Integral directa
P_integral = integrate(f_x_final, (x, 1, Rational(5,2)))
print(f"Método 1 (integral directa):")
print(f"P(1 ≤ x ≤ 2.5) = ∫[1,2.5] f(x) dx")
print(f"               = {P_integral}")
print(f"               = {float(P_integral):.6f}")

# Método 2: Usando F(x)
P_cdf = F_x_simplified.subs(x, Rational(5,2)) - F_x_simplified.subs(x, 1)
print(f"\nMétodo 2 (función acumulativa):")
print(f"P(1 ≤ x ≤ 2.5) = F(2.5) - F(1)")
print(f"               = {P_cdf}")
print(f"               = {float(P_cdf):.6f}")

# -----------------------------------------------------------------------------
# Paso 5: Valor medio (Esperanza)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 5: Valor medio E[X]")
print("-"*80)

E_X = integrate(x * f_x_final, (x, 0, 6))
print(f"E[X] = ∫[0,6] x·f(x) dx")
print(f"     = {E_X}")
print(f"     = {float(E_X):.4f}")

# -----------------------------------------------------------------------------
# Paso 6: Esperanza de X²
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 6: Esperanza de X²")
print("-"*80)

E_X2 = integrate(x**2 * f_x_final, (x, 0, 6))
print(f"E[X²] = ∫[0,6] x²·f(x) dx")
print(f"      = {E_X2}")
print(f"      = {float(E_X2):.4f}")

# -----------------------------------------------------------------------------
# Paso 7: Varianza
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 7: Varianza")
print("-"*80)

Var_X = E_X2 - E_X**2
print(f"Var(X) = E[X²] - (E[X])²")
print(f"       = {E_X2} - ({E_X})²")
print(f"       = {Var_X}")
print(f"       = {float(Var_X):.4f}")

# Desviación estándar
std_X = sqrt(Var_X)
print(f"\nDesviación estándar σ = √Var(X)")
print(f"                      σ = {std_X}")
print(f"                      σ = {float(std_X):.4f}")


# ==============================================================================
# EJERCICIO 2: EXPERIMENTO DE LANZAR DOS DADOS
# ==============================================================================
print("\n\n" + "="*80)
print("EJERCICIO 2: EXPERIMENTO DE LANZAR DOS DADOS")
print("="*80)
print("Enunciado:")
print("Del experimento de lanzar 2 dados, calcular:")
print("- Función de probabilidad")
print("- Función acumulativa")
print("- Valor medio")
print("- Varianza")
print("\n" + "-"*80)

# -----------------------------------------------------------------------------
# Paso 1: Espacio muestral y distribución de probabilidad
# -----------------------------------------------------------------------------
print("\nPaso 1: Espacio muestral y distribución de probabilidad")
print("-"*80)

# Generar todas las combinaciones posibles
espacio_muestral = [(i, j) for i in range(1, 7) for j in range(1, 7)]
print(f"Total de resultados posibles: {len(espacio_muestral)}")

# Calcular la suma de cada par
sumas = [i + j for i, j in espacio_muestral]

# Contar frecuencias de cada suma
from collections import Counter
frecuencias = Counter(sumas)

# Crear distribución de probabilidad
probabilidades = {}
for suma, freq in sorted(frecuencias.items()):
    probabilidades[suma] = Rational(freq, 36)

print("\nDistribución de probabilidad P(X=x):")
print("-"*80)
print(f"{'Suma (x)':<10} {'Combinaciones':<15} {'P(X=x)':<15} {'Decimal'}")
print("-"*80)
for suma, prob in probabilidades.items():
    print(f"{suma:<10} {frecuencias[suma]:<15} {str(prob):<15} {float(prob):.4f}")
print("-"*80)

# Verificar que suma 1
suma_prob = sum(probabilidades.values())
print(f"Suma de probabilidades: {suma_prob} = {float(suma_prob)}")

# -----------------------------------------------------------------------------
# Paso 2: Función acumulativa F(x)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 2: Función acumulativa F(x) = P(X ≤ x)")
print("-"*80)

acumulativas = {}
acum = Rational(0)
print(f"{'x':<10} {'F(x) = P(X≤x)':<20} {'Decimal'}")
print("-"*80)
for suma in sorted(probabilidades.keys()):
    acum += probabilidades[suma]
    acumulativas[suma] = acum
    print(f"{suma:<10} {str(acum):<20} {float(acum):.4f}")
print("-"*80)

# -----------------------------------------------------------------------------
# Paso 3: Valor medio (Esperanza)
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 3: Valor medio E[X]")
print("-"*80)

E_X_dados = sum(x * p for x, p in probabilidades.items())
print(f"E[X] = Σ x·P(X=x)")
print("\nCálculo detallado:")
for x, p in probabilidades.items():
    contribucion = x * p
    print(f"  {x} × {p} = {contribucion} = {float(contribucion):.4f}")
print("-"*80)
print(f"E[X] = {E_X_dados}")
print(f"E[X] = {float(E_X_dados):.4f}")

# -----------------------------------------------------------------------------
# Paso 4: Varianza
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Paso 4: Varianza Var(X)")
print("-"*80)

# Calcular E[X²]
E_X2_dados = sum(x**2 * p for x, p in probabilidades.items())
print(f"E[X²] = Σ x²·P(X=x) = {E_X2_dados} = {float(E_X2_dados):.4f}")

# Calcular varianza
Var_X_dados = E_X2_dados - E_X_dados**2
print(f"\nVar(X) = E[X²] - (E[X])²")
print(f"       = {E_X2_dados} - ({E_X_dados})²")
print(f"       = {Var_X_dados}")
print(f"       = {float(Var_X_dados):.4f}")

# Desviación estándar
std_X_dados = sqrt(Var_X_dados)
print(f"\nDesviación estándar σ = √Var(X)")
print(f"                      σ = {std_X_dados}")
print(f"                      σ = {float(std_X_dados):.4f}")

# -----------------------------------------------------------------------------
# Tabla resumen de varianza
# -----------------------------------------------------------------------------
print("\n" + "-"*80)
print("Tabla detallada para cálculo de varianza:")
print("-"*80)
print(f"{'x':<8} {'P(X=x)':<12} {'(x-μ)²':<12} {'P(X=x)×(x-μ)²':<15}")
print("-"*80)
suma_var = Rational(0)
mu = E_X_dados
for x, p in probabilidades.items():
    desviacion_cuad = (x - mu)**2
    contribucion_var = p * desviacion_cuad
    suma_var += contribucion_var
    print(f"{x:<8} {str(p):<12} {float(desviacion_cuad):<12.4f} {float(contribucion_var):<15.4f}")
print("-"*80)
print(f"Suma (Varianza): {float(suma_var):.4f}")


# ==============================================================================
# RESUMEN DE RESULTADOS
# ==============================================================================
print("\n\n" + "="*80)
print("RESUMEN DE RESULTADOS")
print("="*80)

print("\nEJERCICIO 1: FUNCIÓN DE DENSIDAD CONTINUA f(x) = kx²")
print(f"  - Valor de k:           {float(k_value):.6f}")
print(f"  - P(1 ≤ x ≤ 2.5):       {float(P_integral):.6f}")
print(f"  - Valor medio E[X]:     {float(E_X):.4f}")
print(f"  - E[X²]:                {float(E_X2):.4f}")
print(f"  - Varianza Var(X):      {float(Var_X):.4f}")
print(f"  - Desviación estándar:  {float(std_X):.4f}")

print("\nEJERCICIO 2: SUMA DE DOS DADOS")
print(f"  - Valor medio E[X]:     {float(E_X_dados):.4f}")
print(f"  - E[X²]:                {float(E_X2_dados):.4f}")
print(f"  - Varianza Var(X):      {float(Var_X_dados):.4f}")
print(f"  - Desviación estándar:  {float(std_X_dados):.4f}")

print("\n" + "="*80)
print("FIN DEL TALLER 2")
print("="*80)
