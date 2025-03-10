def detectar_nomes(texto):
    # Dividir o texto em palavras
    palavras = texto.split()

    # Lista para armazenar as sequências encontradas
    sequencias = []

    # Iterar sobre as palavras, verificando pares de palavras
    for i in range(len(palavras) - 1):
        palavra1 = palavras[i]
        palavra2 = palavras[i + 1]
        if palavra1.isalpha() and palavra2.isalpha():
            # Verificar se a primeira palavra tem 4 letras e a segunda tem 6 ou 7 letras
            if len(palavra1) == 4 and len(palavra2) in [6, 7] or (len(palavra1) == 6 and len(palavra2) == 6):
                sequencias.append((palavra1.capitalize(), palavra2.capitalize()))

    return sequencias

