"""
## 5. Percorrendo dicionários
### Explicação
Dicionários armazenam pares chave–valor.

### Exemplo
```python
dados = {"nome": "Gil", "idade": 40}
for chave, valor in dados.items():
    print(chave, valor)
```

### Exercícios
2. Exiba todas as chaves e valores.
"""

dados = {"nome": "Gil", "idade": 61}

for chave, valor in dados.items():
    print(chave, valor)