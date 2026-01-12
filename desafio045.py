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
2. Exiba índice e valor de uma lista de números.
"""

lista = [0,1,2,3,4,5,6,7,8,9]

for indice, valor in enumerate(lista, start=1):
    print(indice, valor)