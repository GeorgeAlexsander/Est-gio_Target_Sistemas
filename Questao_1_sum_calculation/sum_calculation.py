# Sum Calculation

## Descrição da Atividade

Este programa calcula a soma dos números inteiros de 1 até um índice definido (neste caso, 13). A lógica é implementada usando um loop `while`, que itera até que um contador (`K`) atinja o valor do índice. Durante cada iteração, o valor de `K` é adicionado à variável `SOMA`.

## Objetivo

O objetivo desta atividade é demonstrar o uso de estruturas de repetição e variáveis em Python para realizar cálculos simples. Ao final da execução, o programa imprime o resultado da soma.

## Código

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:26:17 2024

@author: georg
"""

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)