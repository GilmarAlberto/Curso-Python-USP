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
2. Use `break` ao encontrar o número 7.
"""

for n in range(10):
    if n == 7:
        break
    print(n)