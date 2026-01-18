"""
## 8. List Comprehension
### Explicação
Forma compacta de criar listas.

### Exemplo
```python
quadrados = [x*x for x in range(5)]
```

### Exercícios
1. Gere uma lista com números pares até 20.
"""

pares = [x for x in range(21) if x % 2 == 0]
print(pares)
