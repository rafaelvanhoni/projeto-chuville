from pathlib import Path
import pandas as pd

# Cidades que vamos manter na versão tratada
CIDADES_DESEJADAS = {
    'SC': ['JOINVILLE', 'SÃO FRANCISCO DO SUL', 'JARAGUÁ DO SUL', 'FLORIANÓPOLIS', 'BALNEÁRIO CAMBORIÚ'],
    'PR': ['CURITIBA', 'PARANAGUÁ'],
    'SP': ['SÃO PAULO']
}

# Pasta com os dados Brutos
PASTA_BRUTA = Path('dados_brutos')

# Lista de arquivos CSV dentro de subpastas por estado
arquivos_csv = list(PASTA_BRUTA.glob("*/*.csv"))
print(f"🔍 Total de arquivos encontrados: {len(arquivos_csv)}")

# Dicionário para armazenar dados por estado e ano
dados_filtrados = {}

for caminho_csv in arquivos_csv:
    estado = caminho_csv.parent.name

    # Se o estado não estiver na lista cidades desejadas, ignora
    if estado not in CIDADES_DESEJADAS:
        continue

    try:
        df = pd.read_csv(caminho_csv, sep=';',encoding='utf-8')
        if 'municipio' not in df.columns or 'datahora' not in df.columns:
            print(f"⚠️ Ignorado (colunas faltando): {caminho_csv.name}")
            continue

        # Filtra as cidades desejadas para esse estado
        cidades = CIDADES_DESEJADAS[estado]
        df_filtrado = df[df['municipio'].isin(cidades)]

        if df_filtrado.empty:
            continue

        # Extrai ano da primeira linha válida
        ano = pd.to_datetime(df_filtrado['datahora'].iloc[0]).year

        # Chave do dicionário: (estado, ano)
        chave = (estado, ano)

        if chave not in dados_filtrados:
            dados_filtrados[chave] = []

        dados_filtrados[chave].append(df_filtrado)

    except Exception as e:
        print(f"❌ Erro ao processar {caminho_csv.name}: {e}")

# Dicionário final com DataFrames unidos
dados_unificados = {}

for chave, lista_df in dados_filtrados.items():
    df_unificado = pd.concat(lista_df, ignore_index=True)
    dados_unificados[chave] = df_unificado

# Cria pasta de saída
pasta_saida = Path('dados_tratados')
pasta_saida.mkdir(exist_ok=True)

for (estado, ano), df in dados_unificados.items():
    pasta_estado = pasta_saida / estado
    pasta_estado.mkdir(exist_ok=True)

    # Ordena dados antes de salvar
    df.sort_values(by=['municipio', 'nomeEstacao', 'datahora'], inplace=True)

    caminho_saida = pasta_estado / f"{ano}.csv"
    df.to_csv(caminho_saida, index=False, sep=';', encoding='utf-8')
    print(f"✅ Arquivo salvo: {caminho_saida}")
