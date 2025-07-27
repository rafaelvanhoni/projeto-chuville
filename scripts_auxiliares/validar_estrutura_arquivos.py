from pathlib import Path
import pandas as pd

def extrair_info_arquivo(nome_arquivo: str) -> list[str, int, int] | list[None, None, None]:
    """
    Extrai UF, ano e mês a partir do nome do arquivo.
    Ex: SC_2022_09.csv -> ('SC', 2022, 9)
    """
    nome = nome_arquivo.stem
    try:
        uf, ano, mes = nome.split('_')
        return uf.upper(), int(ano), int(mes)
    except ValueError:
        print(f"⚠️ Erro ao extrair info de {nome}")
        return None, None, None
    
def extrai_ano_mes(datatime_str: str) -> tuple[int, int]:
    """
    Extrai ano e mês de uma string 'datahora' no formato yyyy-mm-dd HH:MM:SS
    """
    try:
        dt = pd.to_datetime(datatime_str, dayfirst=False)
        return dt.year, dt.month
    except Exception:
        return None, None

def validar_arquivo(caminho_arquivo: Path) -> bool:
    uf_nome, ano_nome, mes_nome = extrair_info_arquivo(caminho_arquivo)

    if None in (uf_nome, ano_nome, mes_nome):
        print(f"⚠️ Nome inválido: {caminho_arquivo.name}")
        return False
    
    try:
        df = pd.read_csv(caminho_arquivo, sep=';', encoding='utf-8')
        if 'datahora' not in df.columns or df.empty:
            print(f"⚠️ Arquivo vazio ou sem coluna 'datahora': {caminho_arquivo.name}")
            return False
        
        # Pega as datas da primeira e última linha (ignora dados fora de ordem)
        data_inicio = pd.to_datetime(df['datahora'].iloc[0])
        data_fim = pd.to_datetime(df['datahora'].iloc[-1])

        ano_conteudo_ini, mes_conteudo_ini = data_inicio.year, data_inicio.month
        ano_conteudo_fim, mes_conteudo_fim = data_fim.year, data_fim.month

        # Valida se o ano e o mês do nome batem com início e fim
        if (ano_nome == ano_conteudo_ini == ano_conteudo_fim) and (mes_nome == mes_conteudo_ini == mes_conteudo_fim):
            return True
        else:
            print(f"❌ Inconsistência no arquivo: {caminho_arquivo.name}")
            print(f"  - Nome: {ano_nome}-{mes_nome}")
            print(f"  - Conteúdo: {ano_conteudo_ini}-{mes_conteudo_ini} até {ano_conteudo_fim}-{mes_conteudo_fim}")
            return False
    except Exception as e:
        print(f"❌ Erro ao processar {caminho_arquivo.name}: {e}")
        return False
    


# Caminho base da pasta onde estão os arquivos organizados por estado
pasta_dados = Path('dados_brutos')

# Verifica se a pasta existe
if not pasta_dados.exists() or not pasta_dados.is_dir():
    print('❌ Pasta dados_brutos/ não encontrada.')
    exit()

# Lista todos os arquivos CSV dentro da subpasta de estado
arquivos_csv = list(pasta_dados.glob("*/*.csv"))
print(f"🔎 {len(arquivos_csv)} arquivos encontrados.")

# Inicio da validação
print(f"\n🧾 Iniciando validação de todos os arquivos...\n")

total_ok = 0
total_erro = 0
arquivos_com_erro = []

for arquivo in arquivos_csv:
    if validar_arquivo(arquivo):
        total_ok += 1
    else:
        total_erro += 1
        arquivos_com_erro.append(arquivo.name)

print("\n✅ Arquivos válidos:", total_ok)
print("\n❌ Arquivos com erro:", total_erro)

if arquivos_com_erro:
    print("\n📂 Lista de arquivos com erro:")
    for nome in arquivos_com_erro:
        print("  - ", nome)

