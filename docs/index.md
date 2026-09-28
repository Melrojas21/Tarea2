# Cuadratura Gaussiana

Este módulo implementa el método de cuadratura Gaussiana con polinomios de Legendre para calcular integrales definidas de forma numérica.

## Problema

Se desea evaluar la integral

$$
I = \int_1^3 \mathrm{d}x \left[ x^6 - x^2 \sin(2x) \right].
$$

El valor exacto se obtiene analíticamente con la primitiva del integrando:

$$
I = \left[ \frac{x^7}{7} + \frac{x^2 \cos(2x)}{2} - \frac{x \sin(2x)}{2} - \frac{\cos(2x)}{4} \right]_1^3 \approx 317.344246673826.
$$

## Objetivo

Aproximar $I$ con cuadratura Gaussiana y determinar el número de puntos de muestreo $N$ con el cual el resultado numérico coincide con el valor exacto dentro de la precisión de máquina.

## Contenido

- [Explicación](explanation.md): fundamento del método numérico.
- [Tutorial](tutorials.md): ejemplo de uso del módulo.
- [Referencia](reference.md): documentación de las funciones.
