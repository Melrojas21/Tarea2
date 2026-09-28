# Tutorial

## Cálculo con un valor de N

Para integrar $x^6 - x^2 \sin(2x)$ entre 1 y 3 con $N = 10$ puntos:

```python
from cuadrature import cuadratura_gaussiana, integrando, valor_exacto

resultado = cuadratura_gaussiana(integrando, 1.0, 3.0, 10)
exacto = valor_exacto(1.0, 3.0)

print(resultado)
print(exacto)
```

Salida:

```text
317.3442466738264
317.34424667382643
```

## Convergencia al aumentar N

Para determinar con cuál valor de $N$ se alcanza el resultado exacto, se repite el cálculo con distintos valores de $N$ y se compara con el valor exacto:

```python
from cuadrature import cuadratura_gaussiana, integrando, valor_exacto

exacto = valor_exacto(1.0, 3.0)

for numero_puntos in range(2, 11):
    resultado = cuadratura_gaussiana(integrando, 1.0, 3.0, numero_puntos)
    print(numero_puntos, resultado, abs(resultado - exacto))
```

Resultados:

| $N$ | Resultado | Error absoluto |
|----:|----------:|---------------:|
| 2 | 306.819934495920 | $1.05 \times 10^{1}$ |
| 3 | 317.264151733829 | $8.01 \times 10^{-2}$ |
| 4 | 317.345390334158 | $1.14 \times 10^{-3}$ |
| 5 | 317.344226721969 | $2.00 \times 10^{-5}$ |
| 6 | 317.344246889996 | $2.16 \times 10^{-7}$ |
| 7 | 317.344246672226 | $1.60 \times 10^{-9}$ |
| 8 | 317.344246673835 | $8.98 \times 10^{-12}$ |
| 9 | 317.344246673826 | $2.27 \times 10^{-13}$ |
| 10 | 317.344246673826 | $5.68 \times 10^{-14}$ |

Con $N = 10$ el error es del orden de la precisión de máquina, por lo que este es el primer valor de $N$ que da el resultado exacto. El término $x^6$ se integra exactamente desde $N = 4$ (pues $2N - 1 = 7 \geq 6$), pero $x^2 \sin(2x)$ no es un polinomio, por lo que su aproximación mejora de forma gradual.

## Ejecución como script

```bash
python cuadrature.py
```
