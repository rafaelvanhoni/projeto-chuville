import os
from pathlib import Path

pasta_base = Path("dados_brutos")

print("Existe?", pasta_base.exists())
print("É diretório?", pasta_base.is_dir())

print("Conteúdo:")
for item in pasta_base.iterdir():
    print("-", item)

print("Caminho absoluto:", pasta_base.resolve())

for pasta_estado in pasta_base.iterdir():
    if pasta_estado.is_dir():
        for arquivo in pasta_estado.iterdir():
            if arquivo.is_file() and arquivo.suffix == '.csv':
                partes = arquivo.stem.split('_')
                if len(partes) == 3:
                    estado, mes, ano = partes
                    novo_nome = f"{estado}_{ano}_{mes}.csv"
                    novo_caminho = arquivo.parent / novo_nome

                    arquivo.rename(novo_caminho)
                    print(f"Renomeado: {arquivo.name} -> {novo_nome}")

