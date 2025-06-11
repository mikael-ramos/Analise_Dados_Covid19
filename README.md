# 📊 Dashboard de Análise de Dados COVID-19

Este projeto é um painel interativo construído com [Streamlit](https://streamlit.io/) para visualizar dados da COVID-19 por país. O objetivo é facilitar a análise exploratória de casos confirmados em diferentes regiões.

## 🚀 Demonstração

O painel permite:

* Selecionar múltiplos países para comparação.
* Visualizar um gráfico de barras com os casos confirmados por país.

## 📁 Estrutura do Projeto

```
├── app.py                 # Script principal com a interface do dashboard
├── dados_covid.csv        # Base de dados com informações da COVID-19
└── requirements.txt       # Dependências do projeto
```

## ⚙️ Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. Crie um ambiente virtual e ative-o (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Como Executar

No terminal, execute:

```bash
streamlit run app.py
```

O navegador abrirá automaticamente o painel interativo.

## 📈 Exemplo de Visualização

* Gráfico de barras com número de casos confirmados por país.
* Filtro interativo para escolha de países.


---


