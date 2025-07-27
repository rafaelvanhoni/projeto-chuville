# ☁️📊 Projeto Chuville – Análise de Precipitação e Storytelling Climático

Este projeto foi desenvolvido como trabalho final da disciplina **IAA007 – Visualização de Dados e Storytelling**, no curso de **Pós-Graduação em Inteligência Artificial Aplicada (UFPR)**.

O objetivo principal é investigar, com base em dados reais, se a cidade de **Joinville (SC)** faz jus ao seu famoso apelido de **“Chuville”**. Através de análise exploratória, tratamento de dados e visualizações narrativas, buscamos validar (ou refutar) a percepção popular com base em **evidências estatísticas**.

---

## 🌧️ Contexto

Joinville é conhecida por seu clima frequentemente nublado e úmido. Mas será que chove mais ali do que em outras cidades do Sul do Brasil? Este projeto analisa dados de precipitação de **sete municípios** entre os anos de **2022 a 2024**, usando fontes oficiais.

---

## 🗂️ Estrutura do Projeto

```
PROJETO_CHUVILLE/
├── dados_brutos/               # Dados originais (ZIP incluído com os arquivos CSVs)
├── dados_tratados/            # Dados tratados por estado (ZIP incluído com os arquivos CSVs)
├── imagens/                    # Gráficos gerados
├── notebooks/
│   └── exploracao_dados.ipynb  # Notebook com análise completa
├── scripts_auxiliares/         # Scripts Python auxiliares
├── relatorio/
│   └── IAA007 - Projeto Chuville - Rafael Vanhoni.pdf  # Versão final do trabalho
├── requirements.txt
└── README.md
```

---

## 📊 Ferramentas Utilizadas

- **Python 3.13.1**
- Bibliotecas: `pandas`, `matplotlib`, `seaborn`, `jupyter`
- Visual Studio Code com extensão Jupyter
- Dados públicos do **CEMADEN** (Centro Nacional de Monitoramento e Alertas de Desastres Naturais)

---

## 🧪 Executando o Notebook

1. Clone o repositório:
```bash
git clone https://github.com/rafaelvanhoni/projeto-chuville.git
```

2. Crie um ambiente virtual (opcional):
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Abra o notebook:
```bash
jupyter notebook notebooks/exploracao_dados.ipynb
```

---

## 📥 Acesso aos Dados Brutos e Tratados (1.05 GB)

Os arquivos CSV completos, incluindo dados originais e tratados por estado, não foram incluídos neste repositório por questões de espaço.

Você pode baixá-los diretamente pelo link abaixo:

🔗 [Google Drive – Dados Brutos e Tratados](https://drive.google.com/drive/folders/16lLWysR7aevQwSmIUmwZzntpWosB58mj?usp=drive_link)

---

## 📄 Relatório Final

O relatório estilizado no formato de jornal (*Joinville Times*) apresenta os principais insights e visualizações da análise, com foco na narrativa climática.

📎 Acesse diretamente:
[IAA007 - Projeto Chuville - Rafael Vanhoni.pdf](relatorio/IAA007%20-%20Projeto%20Chuville%20-%20Rafael%20Vanhoni.pdf)

---

## 👨‍💻 Autor

**Rafael Vanhoni**  
Pós-graduando em Inteligência Artificial Aplicada (UFPR)  
[linkedin.com/in/rafaelvanhoni](https://linkedin.com/in/rafaelvanhoni)

---

## 📝 Licença

Este projeto está licenciado sob a [MIT License](LICENSE), exceto pelos dados públicos que pertencem às suas respectivas fontes.
