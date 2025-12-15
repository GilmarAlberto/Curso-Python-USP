"""
## 3. Percorrendo listas
### Explicação
Listas são coleções ordenadas.

### Exemplo
```python
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print(fruta)
```

### Exercícios
2. Dada uma lista de números, imprima os maiores que 10.

"""

numeros = [1, 20, 2, 19, 3, 18, 4, 17, 5, 16, 6, 15, 7, 14, 8, 13, 9, 12, 10, 11]

for numero in (numeros):

    if numero > 10:
        print(numero)