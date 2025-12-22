"""
## 4. Percorrendo strings
### Explicação
Strings são sequências de caracteres.

### Exemplo
```python
for letra in "Python":
    print(letra)
```

### Exercícios
1. Conte quantas vogais existem em uma palavra.
"""

contador = 0 
for letra in "Gilmar":
    if letra.lower() in "aeiou":
        contador += 1

print(contador)