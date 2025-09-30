# 🎬 Dashboard de Análise Exploratória dos Dados da Netflix

Este projeto apresenta um dashboard interativo completo de análise exploratória dos dados da Netflix usando Streamlit, com visualizações interativas, storytelling com dados e design profissional baseado nos princípios do livro "Storytelling com Dados".

## 📊 Visualizações Incluídas

- **Distribuição de Filmes e Séries** - Gráfico de barras com métricas, percentuais e total geral
- **Adição de Conteúdo ao Longo do Tempo** - Análise temporal de adições com tendências
- **Top 10 Países** - Países com mais conteúdo na plataforma
- **Top Gêneros** - Gêneros mais populares na Netflix
- **Top 10 Diretores** - Diretores com mais títulos na plataforma
- **Top 10 Elenco** - Atores/atrizes com mais participações

## 🎨 Design e Storytelling

- **Paleta de Cores**: Azul profissional (#1f77b4) e cinza (#808080)
- **Layout Limpo**: Design profissional e minimalista
- **Tipografia**: Fonte Arial para melhor legibilidade
- **Responsivo**: Adapta-se a diferentes tamanhos de tela
- **Storytelling**: Textos descritivos em cada visualização explicando insights dos dados
- **Interface Intuitiva**: Navegação clara e organizada

## 🚀 Como Executar

### **🌐 Acesse o Dashboard Online:**
**[🎬 Dashboard Netflix - Streamlit Cloud](https://netflix-daashboard.streamlit.app/)**

### **💻 Executar Localmente:**

1. **Clone o repositório**
```bash
git clone https://github.com/leoserpa/eda-netflix-analysis.git
cd eda-netflix-analysis
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute o dashboard**
```bash
streamlit run app.py
```

## 📁 Estrutura do Projeto

```
eda-netflix-analysis/
├── app.py                 # Dashboard principal Streamlit
├── dataset/
│   └── netflix_titles.csv # Dataset da Netflix (8.709 títulos)
├── notebook/
│   └── netflix.ipynb     # 📓 Notebook de análise exploratória (FUNDAMENTAL)
├── requirements.txt       # Dependências Python
├── .gitignore            # Arquivos ignorados pelo Git
├── LICENSE               # Licença MIT
└── README.md             # Este arquivo
```

### 📓 Sobre o Notebook

O arquivo `notebook/netflix.ipynb` é **essencial** para este projeto, pois contém:
- **Análise exploratória completa** dos dados
- **Tratamento e limpeza** de dados (valores nulos, tipos de dados)
- **Descoberta de insights** e padrões nos dados
- **Desenvolvimento das visualizações** antes da implementação no Streamlit
- **Processo de storytelling** com dados
- **Documentação completa** do processo de análise

## 📈 Dados e Insights

> **💡 Nota Importante**: Este projeto foi desenvolvido através de uma análise exploratória completa realizada no notebook `netflix.ipynb`, que foi fundamental para a descoberta de insights, tratamento de dados e criação das visualizações. O notebook contém todo o processo de exploração, limpeza e análise dos dados antes da implementação do dashboard.

O dataset contém **8.709 títulos** da Netflix incluindo:
- **Tipo**: 70.4% filmes e 29.6% séries
- **Título, diretor, elenco**
- **País de produção** (EUA lidera, seguido por Índia e Reino Unido)
- **Data de adição** (crescimento significativo a partir de 2015)
- **Ano de lançamento**
- **Classificação etária**
- **Duração**
- **Gêneros** (Filmes Internacionais, Dramas e Comédias são os mais populares)
- **Descrição**

### Principais Insights:
- **Anupam Kher** domina o catálogo com 43 títulos
- **EUA** lidera em produção, seguido por **Índia** e **Reino Unido**
- **Crescimento exponencial** de conteúdo entre 2015-2020
- **Foco em diversidade cultural** com gêneros internacionais

## 🛠️ Tecnologias Utilizadas

- **Streamlit** - Framework para aplicações web interativas
- **Pandas** - Manipulação e análise de dados
- **Plotly** - Visualizações interativas e responsivas
- **Python** - Linguagem de programação principal

## 📚 Referências

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Python Documentation](https://plotly.com/python/)
- "Storytelling com Dados" - Cole Nussbaumer Knaflic
- [Netflix Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir melhorias
- Adicionar novas visualizações
- Melhorar a documentação
- Adicionar novos insights

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 👨‍💻 Desenvolvedor

**Leonardo Serpa** 

