"""
Taller 4 - Ejercicios de Estadística
Distribuciones: Poisson, Normal, Binomial y Exponencial
Autor: Contreras Yepes Juan Diego - 20211020069
Universidad Distrital Francisco José de Caldas
"""

from sympy import symbols, exp, factorial, N
from sympy.stats import Poisson, Normal, Binomial, Exponential, P

print("="*70)
print("TALLER 4 - EJERCICIOS DE ESTADÍSTICA CON SYMPY")
print("="*70)

# ==============================================================================
# EJERCICIO 1: LLEGADA DE CLIENTES POR HORA (POISSON)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 1: LLEGADA DE CLIENTES POR HORA (POISSON)")
print("="*70)
print("Enunciado:")
print("El número de clientes que llegan por hora a una tienda sigue una")
print("distribución de Poisson con tasa promedio λ = 5.")
print("¿Cuál es la probabilidad de que lleguen exactamente 3 clientes en una hora?")
print("\nFórmula: P(X = x) = (e^(-λ) * λ^x) / x!")
print("-"*70)

# Método 1: Cálculo manual con fórmula
lmbda_1, x_1 = 5, 3
P_manual_1 = (exp(-lmbda_1) * lmbda_1**x_1) / factorial(x_1)
print(f"Método 1 (fórmula manual): P(X=3) = {N(P_manual_1, 6)}")

# Método 2: Usando SymPy Stats
X1 = Poisson('X1', 5)
P_sympy_1 = P(X1.eq(3))
print(f"Método 2 (SymPy Stats):    P(X=3) = {N(P_sympy_1, 6)}")
print(f"\nResultado: La probabilidad es {float(N(P_manual_1, 4))*100:.2f}%")


# ==============================================================================
# EJERCICIO 2: NÚMERO DE DEFECTOS EN UNA PIEZA (POISSON)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 2: NÚMERO DE DEFECTOS EN UNA PIEZA (POISSON)")
print("="*70)
print("Enunciado:")
print("El número de defectos por pieza fabricada tiene una distribución")
print("de Poisson con media λ = 2.")
print("¿Cuál es la probabilidad de que haya más de un defecto?")
print("\nFórmula: P(X > 1) = 1 - [P(X=0) + P(X=1)]")
print("-"*70)

# Método 1: Cálculo manual
lmbda_2 = 2
P0 = (exp(-lmbda_2) * lmbda_2**0) / factorial(0)
P1 = (exp(-lmbda_2) * lmbda_2**1) / factorial(1)
P_gt1_manual = 1 - (P0 + P1)
print(f"P(X=0) = {N(P0, 6)}")
print(f"P(X=1) = {N(P1, 6)}")
print(f"Método 1 (manual): P(X>1) = {N(P_gt1_manual, 6)}")

# Método 2: Usando SymPy Stats
X2 = Poisson('X2', 2)
P_gt1_sympy = P(X2 > 1)
print(f"Método 2 (SymPy):  P(X>1) = {N(P_gt1_sympy, 6)}")
print(f"\nResultado: La probabilidad es {float(N(P_gt1_manual, 4))*100:.2f}%")


# ==============================================================================
# EJERCICIO 3: CALIFICACIONES DE EXAMEN (NORMAL)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 3: CALIFICACIONES DE EXAMEN (NORMAL)")
print("="*70)
print("Enunciado:")
print("Las calificaciones siguen una distribución normal con media μ = 70")
print("y desviación estándar σ = 8.")
print("¿Cuál es la probabilidad de que un estudiante tenga calificación")
print("entre 65 y 80?")
print("\nFórmula: P(65 < X < 80) = Φ((80-μ)/σ) - Φ((65-μ)/σ)")
print("-"*70)

X3 = Normal('X3', 70, 8)
prob_3 = P((X3 > 65) & (X3 < 80))
print(f"μ = 70, σ = 8")
print(f"z1 = (65-70)/8 = {(65-70)/8:.4f}")
print(f"z2 = (80-70)/8 = {(80-70)/8:.4f}")
print(f"P(65 < X < 80) = {prob_3.evalf(6)}")
print(f"\nResultado: La probabilidad es {float(prob_3.evalf(4))*100:.2f}%")


# ==============================================================================
# EJERCICIO 4: TIEMPO DE PRODUCCIÓN (NORMAL)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 4: TIEMPO DE PRODUCCIÓN (NORMAL)")
print("="*70)
print("Enunciado:")
print("El tiempo de producción sigue una distribución normal con media")
print("μ = 45 minutos y desviación estándar σ = 12 minutos.")
print("¿Cuál es la probabilidad de que el tiempo sea menor a 40 minutos?")
print("\nFórmula: P(X < 40) = Φ((40-μ)/σ)")
print("-"*70)

X4 = Normal('X4', 45, 12)
prob_4 = P(X4 < 40)
print(f"μ = 45, σ = 12")
print(f"z = (40-45)/12 = {(40-45)/12:.4f}")
print(f"P(X < 40) = {prob_4.evalf(6)}")
print(f"\nResultado: La probabilidad es {float(prob_4.evalf(4))*100:.2f}%")


# ==============================================================================
# EJERCICIO 5: CONTROL DE CALIDAD (BINOMIAL)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 5: CONTROL DE CALIDAD (BINOMIAL)")
print("="*70)
print("Enunciado:")
print("En una línea de producción, el 10% de los productos son defectuosos.")
print("Si se seleccionan 15 productos al azar, ¿cuál es la probabilidad")
print("de que exactamente 2 sean defectuosos?")
print("\nFórmula: P(X = k) = C(n,k) * p^k * (1-p)^(n-k)")
print("-"*70)

# Método 1: Cálculo manual
n_5, k_5, p_5 = 15, 2, 0.1
from sympy import binomial
P_manual_5 = binomial(n_5, k_5) * (p_5**k_5) * ((1-p_5)**(n_5-k_5))
print(f"n = {n_5}, k = {k_5}, p = {p_5}")
print(f"C(15,2) = {binomial(n_5, k_5)}")
print(f"Método 1 (manual): P(X=2) = {N(P_manual_5, 6)}")

# Método 2: Usando SymPy Stats
X5 = Binomial('X5', 15, 0.1)
prob_5 = P(X5.eq(2))
print(f"Método 2 (SymPy):  P(X=2) = {prob_5.evalf(6)}")
print(f"\nResultado: La probabilidad es {float(prob_5.evalf(4))*100:.2f}%")


# ==============================================================================
# EJERCICIO 6: EXAMEN DE SELECCIÓN MÚLTIPLE (BINOMIAL)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 6: EXAMEN DE SELECCIÓN MÚLTIPLE (BINOMIAL)")
print("="*70)
print("Enunciado:")
print("Un examen tiene 10 preguntas de selección múltiple con 4 opciones")
print("cada una. Si un estudiante responde al azar, ¿cuál es la probabilidad")
print("de que acierte al menos 6 preguntas?")
print("\nFórmula: P(X ≥ 6) = Σ(k=6 a 10) C(n,k) * p^k * (1-p)^(n-k)")
print("-"*70)

X6 = Binomial('X6', 10, 0.25)
prob_6 = P(X6 >= 6)
print(f"n = 10, p = 0.25 (1/4)")
print(f"P(X ≥ 6) = {prob_6.evalf(6)}")
print(f"\nResultado: La probabilidad es {float(prob_6.evalf(4))*100:.4f}%")
print("(Muy baja probabilidad de aprobar respondiendo al azar)")


# ==============================================================================
# EJERCICIO 7: TIEMPO DE ESPERA EN SERVICIO (EXPONENCIAL)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 7: TIEMPO DE ESPERA EN SERVICIO (EXPONENCIAL)")
print("="*70)
print("Enunciado:")
print("El tiempo de espera en un servicio al cliente sigue una distribución")
print("exponencial con media de 5 minutos (λ = 1/5 = 0.2).")
print("¿Cuál es la probabilidad de que un cliente espere menos de 3 minutos?")
print("\nFórmula: P(X < x) = 1 - e^(-λx)")
print("-"*70)

# Método 1: Cálculo manual
lmbda_7, x_7 = 0.2, 3
P_manual_7 = 1 - exp(-lmbda_7 * x_7)
print(f"λ = {lmbda_7}, x = {x_7}")
print(f"Método 1 (manual): P(X<3) = {N(P_manual_7, 6)}")

# Método 2: Usando SymPy Stats
X7 = Exponential('X7', 0.2)
prob_7 = P(X7 < 3)
print(f"Método 2 (SymPy):  P(X<3) = {prob_7.evalf(6)}")
print(f"\nResultado: La probabilidad es {float(prob_7.evalf(4))*100:.2f}%")


# ==============================================================================
# EJERCICIO 8: VIDA ÚTIL DE COMPONENTE ELECTRÓNICO (EXPONENCIAL)
# ==============================================================================
print("\n" + "="*70)
print("EJERCICIO 8: VIDA ÚTIL DE COMPONENTE ELECTRÓNICO (EXPONENCIAL)")
print("="*70)
print("Enunciado:")
print("La vida útil de un componente electrónico sigue una distribución")
print("exponencial con media de 1000 horas (λ = 1/1000 = 0.001).")
print("¿Cuál es la probabilidad de que el componente dure más de 1500 horas?")
print("\nFórmula: P(X > x) = e^(-λx)")
print("-"*70)

# Método 1: Cálculo manual
lmbda_8, x_8 = 0.001, 1500
P_manual_8 = exp(-lmbda_8 * x_8)
print(f"λ = {lmbda_8}, x = {x_8}")
print(f"Método 1 (manual): P(X>1500) = {N(P_manual_8, 6)}")

# Método 2: Usando SymPy Stats
X8 = Exponential('X8', 0.001)
prob_8 = P(X8 > 1500)
print(f"Método 2 (SymPy):  P(X>1500) = {prob_8.evalf(6)}")
print(f"\nResultado: La probabilidad es {float(prob_8.evalf(4))*100:.2f}%")


# ==============================================================================
# RESUMEN DE RESULTADOS
# ==============================================================================
print("\n" + "="*70)
print("RESUMEN DE RESULTADOS")
print("="*70)
print("\nDISTRIBUCIÓN POISSON:")
print(f"  1. P(X=3, λ=5)    = {float(N(P_manual_1, 4))*100:.2f}%")
print(f"  2. P(X>1, λ=2)    = {float(N(P_gt1_manual, 4))*100:.2f}%")

print("\nDISTRIBUCIÓN NORMAL:")
print(f"  3. P(65<X<80, μ=70, σ=8)   = {float(prob_3.evalf(4))*100:.2f}%")
print(f"  4. P(X<40, μ=45, σ=12)     = {float(prob_4.evalf(4))*100:.2f}%")

print("\nDISTRIBUCIÓN BINOMIAL:")
print(f"  5. P(X=2, n=15, p=0.1)     = {float(prob_5.evalf(4))*100:.2f}%")
print(f"  6. P(X≥6, n=10, p=0.25)    = {float(prob_6.evalf(4))*100:.4f}%")

print("\nDISTRIBUCIÓN EXPONENCIAL:")
print(f"  7. P(X<3, λ=0.2)           = {float(prob_7.evalf(4))*100:.2f}%")
print(f"  8. P(X>1500, λ=0.001)      = {float(prob_8.evalf(4))*100:.2f}%")

print("\n" + "="*70)
print("FIN DEL TALLER 4")
print("="*70)
