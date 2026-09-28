"""Módulo de cuadratura Gaussiana con polinomios de Legendre.

Calcula la integral definida de x^6 - x^2 sin(2x) entre 1 y 3 y permite
comparar el resultado numérico con el valor exacto para distintos valores de N.
"""

from typing import Callable

import numpy as np


def gaussxw(numero_puntos: int) -> tuple[np.ndarray, np.ndarray]:
    """Puntos de muestreo y pesos de la cuadratura de Gauss-Legendre.

    Los puntos de muestreo son las raíces del polinomio de Legendre de orden N
    y están definidos en el intervalo [-1, 1].

    Examples:
        >>> puntos, pesos = gaussxw(2)
        >>> puntos.round(6).tolist()
        [-0.57735, 0.57735]
        >>> pesos.round(6).tolist()
        [1.0, 1.0]

    Args:
        numero_puntos (int): Número de puntos de muestreo N.

    Returns:
        tuple: Arreglos de NumPy ``(puntos, pesos)``, ambos de longitud N.

    """
    puntos, pesos = np.polynomial.legendre.leggauss(numero_puntos)
    return puntos, pesos


def gaussxwab(
    limite_inferior: float,
    limite_superior: float,
    puntos: np.ndarray,
    pesos: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    """Escala los puntos y pesos de [-1, 1] al intervalo [a, b].

    Examples:
        >>> puntos, pesos = gaussxw(2)
        >>> puntos_ab, pesos_ab = gaussxwab(1.0, 3.0, puntos, pesos)
        >>> puntos_ab.round(6).tolist()
        [1.42265, 2.57735]
        >>> pesos_ab.round(6).tolist()
        [1.0, 1.0]

    Args:
        limite_inferior (float): Límite inferior a del intervalo.
        limite_superior (float): Límite superior b del intervalo.
        puntos (np.ndarray): Puntos de muestreo en [-1, 1].
        pesos (np.ndarray): Pesos asociados a los puntos en [-1, 1].

    Returns:
        tuple: Arreglos de NumPy ``(puntos_escalados, pesos_escalados)``.

    """
    semiancho = 0.5 * (limite_superior - limite_inferior)
    punto_medio = 0.5 * (limite_superior + limite_inferior)
    return semiancho * puntos + punto_medio, semiancho * pesos


def integrando(x: np.ndarray) -> np.ndarray:
    """Función a integrar, f(x) = x^6 - x^2 sin(2x).

    Examples:
        >>> integrando(np.array([0.0, 1.0])).round(6).tolist()
        [0.0, 0.090703]

    Args:
        x (np.ndarray): Puntos donde se evalúa la función.

    Returns:
        np.ndarray: Valores de f(x) en cada punto.

    """
    return x**6 - x**2 * np.sin(2.0 * x)


def cuadratura_gaussiana(
    funcion: Callable[[np.ndarray], np.ndarray],
    limite_inferior: float,
    limite_superior: float,
    numero_puntos: int,
) -> float:
    """Aproxima la integral de una función en [a, b] con cuadratura Gaussiana.

    Examples:
        >>> round(cuadratura_gaussiana(lambda x: x**2, 0.0, 3.0, 2), 6)
        9.0

    Args:
        funcion (Callable): Función vectorizada que se desea integrar.
        limite_inferior (float): Límite inferior a del intervalo.
        limite_superior (float): Límite superior b del intervalo.
        numero_puntos (int): Número de puntos de muestreo N.

    Returns:
        float: Aproximación de la integral de ``funcion`` entre a y b.

    """
    puntos, pesos = gaussxw(numero_puntos)
    puntos_ab, pesos_ab = gaussxwab(limite_inferior, limite_superior, puntos, pesos)
    return float(np.sum(pesos_ab * funcion(puntos_ab)))


def valor_exacto(limite_inferior: float, limite_superior: float) -> float:
    """Valor analítico de la integral de x^6 - x^2 sin(2x) en [a, b].

    Se evalúa la primitiva F(x) = x^7/7 + x^2 cos(2x)/2 - x sin(2x)/2 - cos(2x)/4
    como F(b) - F(a).

    Examples:
        >>> round(valor_exacto(1.0, 3.0), 6)
        317.344247

    Args:
        limite_inferior (float): Límite inferior a del intervalo.
        limite_superior (float): Límite superior b del intervalo.

    Returns:
        float: Valor exacto de la integral entre a y b.

    """

    def primitiva(x: float) -> float:
        return (
            x**7 / 7.0
            + x**2 * np.cos(2.0 * x) / 2.0
            - x * np.sin(2.0 * x) / 2.0
            - np.cos(2.0 * x) / 4.0
        )

    return float(primitiva(limite_superior) - primitiva(limite_inferior))


if __name__ == "__main__":
    LIMITE_INFERIOR = 1.0
    LIMITE_SUPERIOR = 3.0
    resultado_exacto = valor_exacto(LIMITE_INFERIOR, LIMITE_SUPERIOR)
    print(f"Valor exacto: {resultado_exacto:.15f}\n")
    print(f"{'N':>3} {'Resultado':>20} {'Error absoluto':>16}")

    for numero_puntos in range(2, 13):
        resultado = cuadratura_gaussiana(
            integrando, LIMITE_INFERIOR, LIMITE_SUPERIOR, numero_puntos
        )
        error_absoluto = abs(resultado - resultado_exacto)
        print(f"{numero_puntos:>3} {resultado:>20.15f} {error_absoluto:>16.2e}")
