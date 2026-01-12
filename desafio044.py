"""
## 6. `for` com `enumerate()`
### Explicação
`enumerate()` retorna índice e valor ao mesmo tempo.

### Exemplo
```python
lista = ["a", "b", "c"]
for indice, valor in enumerate(lista):
    print(indice, valor)
```

### Exercícios
1. Exiba índice e nome em uma lista de nomes.
"""

lista = ["Gilmar", "Alberto", "de", "Abreu", "Pinto"]

for indice, valor in enumerate(lista, start=1):
    print(indice, valor)