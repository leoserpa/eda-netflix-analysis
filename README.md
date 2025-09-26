# 🎬 Análise Exploratória - Netflix

Este projeto apresenta uma análise exploratória completa dos dados da Netflix usando Streamlit, com visualizações interativas e design baseado nos princípios do livro "Storytelling com Dados".

## 📊 Visualizações Incluídas

- **Distribuição de Filmes e Séries** - Gráfico de barras com métricas e percentuais
- **Adição de Conteúdo ao Longo do Tempo** - Análise temporal de adições
- **Top 10 Países** - Países com mais conteúdo na plataforma
- **Top Gêneros** - Gêneros mais populares na Netflix

## 🎨 Design

- **Paleta de Cores**: Baseada no "Storytelling com Dados" (azul #1f77b4 e laranja #ff7f0e)
- **Layout Limpo**: Design profissional e minimalista
- **Tipografia**: Fonte Arial para melhor legibilidade
- **Responsivo**: Adapta-se a diferentes tamanhos de tela

## 🚀 Como Executar

### Pré-requisitos
- Python 3.7+
- Streamlit
- Pandas
- Plotly

### Instalação
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/project_netflix.git

# Navegue para o diretório
cd project_netflix

# Instale as dependências
pip install -r requirements.txt

# Execute a aplicação
streamlit run app.py
```

### Acesso
Após executar, acesse: http://localhost:8501

## 📁 Estrutura do Projeto

```
project_netflix/
├── app.py                 # Aplicação principal Streamlit
├── dataset/
│   └── netflix_titles.csv # Dataset da Netflix
├── notebook/
│   └── netflix.ipynb     # Notebook de análise exploratória
├── requirements.txt       # Dependências Python
├── .gitignore            # Arquivos ignorados pelo Git
└── README.md             # Este arquivo
```

## 📈 Dados

O dataset contém informações sobre títulos da Netflix incluindo:
- Tipo (Movie/TV Show)
- Título, diretor, elenco
- País de produção
- Data de adição
- Ano de lançamento
- Classificação etária
- Duração
- Gêneros
- Descrição

## 🛠️ Tecnologias Utilizadas

- **Streamlit** - Framework para aplicações web
- **Pandas** - Manipulação de dados
- **Plotly** - Visualizações interativas
- **Python** - Linguagem de programação

## 📚 Referências

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- "Storytelling com Dados" - Cole Nussbaumer Knaflic

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novas visualizações
- Melhorar a documentação

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

**Desenvolvido com ❤️ usando Streamlit e Python**
