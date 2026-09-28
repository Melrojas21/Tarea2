# Explicación del método

## Idea principal

La cuadratura Gaussiana aproxima una integral definida como una suma ponderada de valores de la función:

$$
\int_a^b \mathrm{d}x \, f(x) \approx \sum_{k=1}^{N} w_k f(x_k),
$$

donde $x_k$ son los puntos de muestreo y $w_k$ los pesos. A diferencia de las reglas de Newton-Cotes, los puntos de muestreo no son equidistantes. Esto añade grados de libertad y permite que el método con $N$ puntos sea exacto para polinomios de grado hasta $2N - 1$.

## Puntos y pesos

Los puntos de muestreo $x_k$ son las $N$ raíces del polinomio de Legendre $P_N(x)$, definido en el intervalo $[-1, 1]$. Los pesos se calculan con

$$
w_k = \left[ \frac{2}{1 - x^2} \left( \frac{\mathrm{d}P_N}{\mathrm{d}x} \right)^{-2} \right]_{x = x_k}.
$$

Los polinomios de Legendre se generan con $P_0(x) = 1$, $P_1(x) = x$ y la relación de recurrencia

$$
(N + 1) P_{N+1}(x) = (2N + 1)\, x\, P_N(x) - N\, P_{N-1}(x).
$$

Son ortogonales en $[-1, 1]$:

$$
\int_{-1}^{1} \mathrm{d}x \, P_N(x) P_M(x) = \frac{2 \delta_{MN}}{2N + 1}.
$$

## Cambio de intervalo

Los puntos y pesos se calculan una sola vez en $[-1, 1]$ y luego se escalan a un intervalo general $[a, b]$:

$$
x_k' = \frac{b - a}{2} x_k + \frac{b + a}{2}, \qquad w_k' = \frac{b - a}{2} w_k.
$$

## Implementación

El módulo usa `numpy.polynomial.legendre.leggauss` para obtener los puntos y pesos en $[-1, 1]$, y una función de escalamiento para llevarlos a $[a, b]$. La suma se realiza con operaciones vectoriales de NumPy.

## Ventajas y limitaciones

- La convergencia es rápida: el error disminuye de forma apreciable al aumentar $N$ en uno.
- Funciona bien con funciones bien comportadas. Si la función no lo es, se requieren más puntos cerca de las regiones problemáticas.
- No existe una expresión sencilla para estimar el error del método.

## Referencia

M. Newman, *Computational Physics*, Capítulo 5 y Apéndice C.
