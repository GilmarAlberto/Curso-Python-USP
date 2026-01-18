"""
Docstring para desafio050
## 9. For aninhado
### Explicação
Um `for` dentro de outro permite gerar combinações.

### Exemplofor i in range(3):
    for j in range(3):
        print(i, j)
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

### Exercícios
1. Gere uma matriz 3×3.
"""
for i in range(3):
    for j in range(3):
        print(f"{i},{j}", end=" ")
    print()

