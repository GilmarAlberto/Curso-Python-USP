'''
Introdução à Ciência da Computação com Python Parte 1
Módulo 9 - Mais sobre listas

Tarefa de programação: Programa completo - Similaridades entre textos - Caso COH-PIAH

Prólogo

Neste último exercício da Parte 1, iremos praticar não só o que vimos até agora no curso mas também outra habilidade importante de um programador: utilizar e interagir com código escrito por terceiros. Aqui, você não irá implementar o seu programa do zero. Você irá partir de um programa já iniciado e irá completá-lo. Na verdade, esse é o caso mais comum na indústria de software, onde muitos desenvolvedores trabalham colaborativamente em um mesmo programa.

https://www.coursera.org/learn/ciencia-computacao-python-conceitos/programming/oUnlk/programa-completo-similaridades-entre-textos-caso-coh-piah
'''

import re

def separa_sentencas(texto):
    # Divide por ., !, ? considerando pontuação final
    sentencas = re.split(r'[.!?]+', texto)
    # Remove vazios e espaços supérfluos
    return [s.strip() for s in sentencas if s.strip()]

def separa_frases(sentenca):
    # Divide por vírgula, ponto e vírgula e dois pontos
    frases = re.split(r'[,:;]+', sentenca)
    return [f.strip() for f in frases if f.strip()]

def separa_palavras(frase):
    # Palavras são tokens separados por espaços
    # Mantém apenas letras e números dentro das palavras
    tokens = frase.split()
    palavras = []
    for t in tokens:
        # remove pontuação acoplada (e.g., "palavra," -> "palavra")
        limpo = re.sub(r'^[^A-Za-z0-9]+|[^A-Za-z0-9]+$', '', t)
        if limpo:
            palavras.append(limpo)
    return palavras

def n_palavras_diferentes(lista_palavras):
    # normaliza para minúsculas
    vistos = set(p.lower() for p in lista_palavras)
    return len(vistos)

def n_palavras_unicas(lista_palavras):
    contagem = {}
    for p in lista_palavras:
        k = p.lower()
        contagem[k] = contagem.get(k, 0) + 1
    return sum(1 for k, v in contagem.items() if v == 1)

def tamanho_medio_palavra(lista_palavras):
    if not lista_palavras:
        return 0.0
    soma = sum(len(p) for p in lista_palavras)
    return soma / len(lista_palavras)

def tamanho_medio_sentenca(sentencas):
    if not sentencas:
        return 0.0
    # tamanho em caracteres das sentenças, sem pontuação final
    soma = sum(len(s) for s in sentencas)
    return soma / len(sentencas)

def complexidade_sentenca(sentencas):
    if not sentencas:
        return 0.0
    total_frases = sum(len(separa_frases(s)) for s in sentencas)
    return total_frases / len(sentencas)

def tamanho_medio_frase(frases):
    if not frases:
        return 0.0
    soma = sum(len(f) for f in frases)
    return soma / len(frases)

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = []
    for s in sentencas:
        frases.extend(separa_frases(s))
    palavras = []
    for f in frases:
        palavras.extend(separa_palavras(f))

    wal = tamanho_medio_palavra(palavras)  # Word Average Length
    ttr = (n_palavras_diferentes(palavras) / len(palavras)) if palavras else 0.0  # Type-Token Ratio
    hlr = (n_palavras_unicas(palavras) / len(palavras)) if palavras else 0.0     # Hapax Legomena Ratio
    sal = tamanho_medio_sentenca(sentencas)  # Sentence Average Length (chars)
    sc = complexidade_sentenca(sentencas)    # Sentence Complexity (phrases per sentence)
    pal = tamanho_medio_frase(frases)        # Phrase Average Length (chars)

    return [wal, ttr, hlr, sal, sc, pal]

def compara_assinaturas(ass1, ass2):
    # distância: média das diferenças absolutas por componente
    if not ass1 or not ass2 or len(ass1) != len(ass2):
        raise ValueError("Assinaturas incompatíveis.")
    difs = [abs(a - b) for a, b in zip(ass1, ass2)]
    return sum(difs) / len(difs)

def avalia_textos(textos, assinatura_suspeita):
    # Retorna índice (1-based) do texto mais parecido com a assinatura suspeita
    melhor_idx = None
    melhor_dist = float('inf')
    for i, t in enumerate(textos, start=1):
        ass_t = calcula_assinatura(t)
        dist = compara_assinaturas(ass_t, assinatura_suspeita)
        if dist < melhor_dist:
            melhor_dist = dist
            melhor_idx = i
    return melhor_idx, melhor_dist

def ler_assinatura_suspeita():
    print("Informe a assinatura suspeita (6 valores):")
    wal = float(input("Tamanho médio de palavra: "))
    ttr = float(input("Relação Type-Token: "))
    hlr = float(input("Razão Hapax Legomena: "))
    sal = float(input("Tamanho médio de sentença: "))
    sc  = float(input("Complexidade de sentença: "))
    pal = float(input("Tamanho médio de frase: "))
    return [wal, ttr, hlr, sal, sc, pal]

def ler_textos():
    print("Digite os textos (linha vazia para encerrar):")
    textos = []
    while True:
        t = input()
        if not t:
            break
        textos.append(t)
    return textos

def main():
    assinatura_suspeita = ler_assinatura_suspeita()
    textos = ler_textos()
    if not textos:
        print("Nenhum texto fornecido.")
        return
    idx, dist = avalia_textos(textos, assinatura_suspeita)
    print(f"Texto {idx} é o mais semelhante à assinatura suspeita (distância = {dist:.4f}).")

if __name__ == "__main__":
    main()
