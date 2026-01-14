"""
## 7. `for` com `break` e `continue`
### Explicação
`break` interrompe o loop; `continue` pula para a próxima iteração.

### Exemplo
```python
for n in range(10):
    if n == 5:
        break
    print(n)
```

### Exercícios
1. Use `continue` para pular números ímpares.
"""

for n in range(10):
    if n%2 != 0:
        continue
    print(n)
