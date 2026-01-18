"""
## 9. For aninhado
### Explicação
Um `for` dentro de outro permite gerar combinações.

### Exemplo
```python
for i in range(3):
    for j in range(3):
        print(i, j)
```

### Exercícios
2. Imprima todas as combinações possíveis entre duas listas.
"""

lista1 = [1,2,3]
lista2 = [4,5,6]

for i in lista1:

    for j in lista2:
        print(i,j)