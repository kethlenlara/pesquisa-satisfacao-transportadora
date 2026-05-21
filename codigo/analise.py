import pandas as pd

# LEITURA DO CSV
dados = pd.read_csv(
    r"C:\Users\Kethlen\OneDrive\Documentos\Faculdade\Projeto Transportadora\dados\respostas.csv"
)

# MOSTRAR DADOS
print("=== DADOS DA PESQUISA ===")
print(dados)

# MÉDIAS
print("\n=== MÉDIAS ===")

print("\nMédia do atendimento:")
print(dados["Atendimento"].mean())

print("\nMédia do motorista:")
print(dados["Motorista"].mean())

print("\nMédia do prazo:")
print(dados["Prazo"].mean())

print("\nMédia da comunicação:")
print(dados["Comunicação"].mean())

print("\nMédia da satisfação geral:")
print(dados["Nota_Geral"].mean())

# PRINCIPAIS PROBLEMAS
print("\n=== PRINCIPAIS PROBLEMAS ===")
print(dados["Problema"].value_counts())


# CLASSIFICAÇÃO DOS COMENTÁRIOS
def classificar_comentario(texto):

    texto = str(texto).lower()

    if "atras" in texto or "demor" in texto:
        return "Atraso"

    elif "comunica" in texto or "avis" in texto:
        return "Comunicação"

    elif "motorista" in texto:
        return "Motorista"

    elif "produto" in texto or "caixa" in texto:
        return "Produto"

    else:
        return "Outros"


dados["Categoria"] = dados["Melhorar"].apply(classificar_comentario)

print("\n=== CATEGORIAS DOS COMENTÁRIOS ===")
print(dados["Categoria"].value_counts())


# ANÁLISE DE SENTIMENTO DOS COMENTÁRIOS
def analisar_sentimento(comentario):

    comentario = str(comentario).lower()

    palavras_positivas = [
        "bom",
        "ótimo",
        "excelente",
        "rápido",
        "educado",
        "certinho",
        "boa"
    ]

    palavras_negativas = [
        "demora",
        "atraso",
        "ruim",
        "problema",
        "amassada",
        "dificuldade"
    ]

    for palavra in palavras_positivas:
        if palavra in comentario:
            return "Positivo"

    for palavra in palavras_negativas:
        if palavra in comentario:
            return "Negativo"

    return "Neutro"


dados["Sentimento_Comentario"] = dados["Comentário"].apply(analisar_sentimento)

print("\n=== SENTIMENTO DOS COMENTÁRIOS ===")
print(dados["Sentimento_Comentario"].value_counts())

dados.to_csv(
    r"C:\Users\Kethlen\OneDrive\Documentos\Faculdade\Projeto Transportadora\dados\resultado_analise.csv",
    index=False
)

print("\nArquivo de análise salvo com sucesso!")