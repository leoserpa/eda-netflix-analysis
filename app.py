import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Análise Netflix",
    page_icon="🎬",
    layout="wide"
)

# Título principal
st.title("🎬 Análise Exploratória - Netflix")
st.markdown("---")

# Carregamento dos dados
@st.cache_data
def load_data():
    df = pd.read_csv('dataset/netflix_titles.csv')
    return df

df = load_data()

# Usar todos os dados sem filtro
df_filtrado = df

# Seção: Métricas Numéricas
st.markdown("<h2 style='text-align: left;'>📊 Métricas Gerais</h2>", unsafe_allow_html=True)

# Calcular métricas
total_filmes = len(df[df['type'] == 'Movie'])
total_series = len(df[df['type'] == 'TV Show'])
total_geral = len(df)

# Exibir métricas em colunas
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🎬 Total de Filmes",
        value=f"{total_filmes:,}",
        delta=f"{(total_filmes/total_geral)*100:.1f}% do total"
    )

with col2:
    st.metric(
        label="📺 Total de Séries",
        value=f"{total_series:,}",
        delta=f"{(total_series/total_geral)*100:.1f}% do total"
    )

with col3:
    st.metric(
        label="📈 Total Geral",
        value=f"{total_geral:,}",
        delta="100%"
    )

st.markdown("---")

# Seção: Distribuição de Filmes e Séries
st.markdown("<h2 style='text-align: left; margin-bottom: 20px;'>📊 Distribuição de Filmes e Séries</h2>", unsafe_allow_html=True)

# Cálculo da distribuição
contagem_tipo = df_filtrado['type'].value_counts().reset_index()
contagem_tipo.columns = ['Tipo', 'Quantidade']

# Calcular percentuais
total_filtrado = len(df_filtrado)
contagem_tipo['Percentual'] = (contagem_tipo['Quantidade'] / total_filtrado * 100).round(1)

# Exibir tabela com percentuais
st.subheader("📋 Resumo Numérico")
col1, col2 = st.columns(2)

with col1:
    st.dataframe(
        contagem_tipo[['Tipo', 'Quantidade']],
        use_container_width=True
    )

with col2:
    st.dataframe(
        contagem_tipo[['Tipo', 'Percentual']],
        use_container_width=True
    )

# Criar o gráfico
figura = px.bar(
    contagem_tipo, 
    x='Tipo', 
    y='Quantidade', 
    title='Distribuição de Filmes e Séries na Netflix',
    color='Tipo',
    color_discrete_sequence=['#1f77b4', '#808080'],  # Azul e cinza como na imagem
    text='Quantidade'
)

# Melhorar o layout seguindo princípios do Storytelling com Dados
figura.update_layout(
    showlegend=False,
    height=500,
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    margin=dict(t=100),
    xaxis_title="Tipo de Conteúdo",
    yaxis_title="Quantidade",
    # Layout mais limpo e profissional
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", size=12),
    title_font_size=16,
    # Remover linhas de grade desnecessárias
    xaxis=dict(
        showgrid=False,
        linecolor='#d3d3d3',
        linewidth=1
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#f0f0f0',
        linecolor='#d3d3d3',
        linewidth=1
    )
)

# Adicionar valores nas barras
figura.update_traces(texttemplate='%{text}', textposition='outside')

# Preparar dados para análise temporal (antes de exibir os gráficos)
df_temp = df_filtrado.copy()
df_temp['date_added'] = pd.to_datetime(df_temp['date_added'], errors='coerce')
df_temp = df_temp.dropna(subset=['date_added'])
df_temp['year_added'] = df_temp['date_added'].dt.year

# Contar o número de títulos adicionados por ano
yearly_adds = df_temp.groupby('year_added').size().reset_index(name='count')

# Criar o gráfico de linha
fig_tempo = px.line(
    yearly_adds, 
    x='year_added', 
    y='count',
    title='Adição de Conteúdo ao Longo do Tempo',
    labels={'year_added': 'Ano', 'count': 'Número de Adições'},
    color_discrete_sequence=['#1f77b4']  # Azul para evolução temporal
)

# Melhorar o layout do gráfico temporal
fig_tempo.update_layout(
    height=500,
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    margin=dict(t=100),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", size=12),
    title_font_size=16,
    xaxis=dict(
        showgrid=True,
        gridcolor='#f0f0f0',
        linecolor='#d3d3d3',
        linewidth=1
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#f0f0f0',
        linecolor='#d3d3d3',
        linewidth=1
    )
)

# Adicionar marcadores nos pontos
fig_tempo.update_traces(
    mode='lines+markers',
    marker=dict(size=6, color='#1f77b4'),
    line=dict(width=3, color='#1f77b4')
)

# Exibir os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='text-align: center; margin-bottom: 15px;'>📊 Distribuição</h3>", unsafe_allow_html=True)
    st.plotly_chart(figura, use_container_width=True)

with col2:
    st.markdown("<h3 style='text-align: center; margin-bottom: 15px;'>📈 Evolução Temporal</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_tempo, use_container_width=True)

st.markdown("---")

# Seção: Conteúdo por País de Produção
st.markdown("<h2 style='text-align: center;'>🌍 Top 10 Países com Mais Conteúdo</h2>", unsafe_allow_html=True)

# Processar dados de países
countries = df_filtrado['country'].str.split(', ', expand=True).stack()
country_counts = countries.value_counts().reset_index(name='count')
country_counts.columns = ['Country', 'Count']
country_counts = country_counts[country_counts['Country'] != 'Não Informado']
top_countries = country_counts.head(10)

# Criar o gráfico de barras
fig_paises = px.bar(
    top_countries, 
    x='Country', 
    y='Count',
    title='Top 10 Países com Mais Conteúdo na Netflix',
    labels={'Country': 'País', 'Count': 'Número de Títulos'},
    color='Count',
    color_continuous_scale=['#1f77b4', '#808080']  # Azul e cinza 
)

# Melhorar o layout
fig_paises.update_layout(
    height=500,
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    margin=dict(t=100),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", size=12),
    title_font_size=16,
    xaxis=dict(
        showgrid=False,
        linecolor='#d3d3d3',
        linewidth=1
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#f0f0f0',
        linecolor='#d3d3d3',
        linewidth=1
    )
)

# Rotacionar labels do eixo X para melhor legibilidade
fig_paises.update_xaxes(tickangle=45)

# Processar dados de gêneros (antes de exibir os gráficos)
genres = df_filtrado['listed_in'].str.split(', ', expand=True).stack()
genre_counts = genres.value_counts().reset_index(name='count')
genre_counts.columns = ['Genre', 'Count']
top_genres = genre_counts.head(15)

# Criar o gráfico de barras de gêneros
fig_generos = px.bar(
    top_genres, 
    x='Genre', 
    y='Count',
    title='Top Gêneros na Netflix',
    labels={'Genre': 'Gênero', 'Count': 'Número de Títulos'},
    color='Count',
    color_continuous_scale=['#1f77b4', '#808080']  # Azul e cinza 
)

# Melhorar o layout do gráfico de gêneros
fig_generos.update_layout(
    height=500,
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    margin=dict(t=100),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", size=12),
    title_font_size=16,
    xaxis=dict(
        showgrid=False,
        linecolor='#d3d3d3',
        linewidth=1,
        categoryorder='total descending'
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#f0f0f0',
        linecolor='#d3d3d3',
        linewidth=1
    )
)

# Rotacionar labels do eixo X
fig_generos.update_xaxes(tickangle=45)

# Exibir os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='text-align: center; margin-bottom: 15px;'>🌍 Top 10 Países</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_paises, use_container_width=True)

with col2:
    st.markdown("<h3 style='text-align: center; margin-bottom: 15px;'>🎭 Top Gêneros</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_generos, use_container_width=True)

st.markdown("---")

# Seção: Top Diretores na Netflix
st.markdown("<h2 style='text-align: center;'>🎬 Top 10 Diretores na Netflix</h2>", unsafe_allow_html=True)

# Processar dados de diretores
directors = df_filtrado['director'].str.split(', ', expand=True).stack()
director_counts = directors.value_counts().reset_index(name='count')
director_counts.columns = ['Director', 'Count']
director_counts = director_counts[director_counts['Director'] != 'Não Informado']
top_directors = director_counts.head(10)

# Criar o gráfico de barras
fig_diretores = px.bar(
    top_directors, 
    x='Director', 
    y='Count',
    title='Top 10 Diretores com Mais Conteúdo na Netflix',
    labels={'Director': 'Diretor', 'Count': 'Número de Títulos'},
    color='Count',
    color_continuous_scale=['#1f77b4', '#808080']  # Azul e cinza 
)

# Melhorar o layout
fig_diretores.update_layout(
    height=500,
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    margin=dict(t=100),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", size=12),
    title_font_size=16,
    xaxis=dict(
        showgrid=False,
        linecolor='#d3d3d3',
        linewidth=1,
        categoryorder='total descending'
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#f0f0f0',
        linecolor='#d3d3d3',
        linewidth=1
    )
)

# Rotacionar labels do eixo X
fig_diretores.update_xaxes(tickangle=45)

# Processar dados de elenco (antes de exibir os gráficos)
cast_members = df_filtrado['cast'].str.split(', ', expand=True).stack()
cast_counts = cast_members.value_counts().reset_index(name='count')
cast_counts.columns = ['Cast Member', 'Count']
cast_counts = cast_counts[cast_counts['Cast Member'] != 'Não Informado']
top_cast = cast_counts.head(10)

# Criar o gráfico de barras de elenco
fig_elenco = px.bar(
    top_cast, 
    x='Cast Member', 
    y='Count',
    title='Top 10 Membros do Elenco na Netflix',
    labels={'Cast Member': 'Membro do Elenco', 'Count': 'Número de Títulos'},
    color='Count',
    color_continuous_scale=['#1f77b4', '#808080']  # Azul e cinza 
)

# Melhorar o layout do gráfico de elenco
fig_elenco.update_layout(
    height=500,
    title_x=0.5,
    title_y=0.95,
    title_xanchor='center',
    title_yanchor='top',
    margin=dict(t=100),
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family="Arial", size=12),
    title_font_size=16,
    xaxis=dict(
        showgrid=False,
        linecolor='#d3d3d3',
        linewidth=1,
        categoryorder='total descending'
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#f0f0f0',
        linecolor='#d3d3d3',
        linewidth=1
    )
)

# Rotacionar labels do eixo X
fig_elenco.update_xaxes(tickangle=45)

# Exibir os gráficos lado a lado
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3 style='text-align: center; margin-bottom: 15px;'>🎬 Top 10 Diretores</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_diretores, use_container_width=True)

with col2:
    st.markdown("<h3 style='text-align: center; margin-bottom: 15px;'>⭐ Top 10 Elenco</h3>", unsafe_allow_html=True)
    st.plotly_chart(fig_elenco, use_container_width=True)

# Informações adicionais
st.info(f"💡 **Dados carregados:** {len(df):,} títulos | **Filtrado:** {len(df_filtrado):,} títulos")
