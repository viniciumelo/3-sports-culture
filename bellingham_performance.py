import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Jude Bellingham
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Retenção, Passe e Condução)', 
    'Velocidade Máxima<br>(Sprints Box-to-Box)', 
    'Chances de Gol<br>(Infiltração, xG e Assistências)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados analíticos)
# Bellingham registra números no topo global de chegada à área e controle de meio-campo, com ótima velocidade.
valores_grafico = [91, 85, 92]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 62+ toques/jogo e força sob pressão)", 
    "33.8 km/h de pico (Intensidade na cobertura e ataques de espaço)", 
    "0.80 xG+xA (Presença constante de área e passes decisivos)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]

# 2. Construção do Gráfico de Radar Interativo
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=valores_grafico_fechados,
    theta=metricas_fechadas,
    fill='toself',
    fillcolor='rgba(255, 215, 0, 0.3)',  # Tom dourado
    line=dict(color='gold', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Jude Bellingham'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Jude Bellingham",
        font=dict(size=22, color='white'),
        x=0.5,
        y=0.95
    ),
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor="rgba(255, 255, 255, 0.2)",
            tickfont=dict(color="rgba(255, 255, 255, 0.7)")
        ),
        angularaxis=dict(
            gridcolor="rgba(255, 255, 255, 0.3)",
            tickfont=dict(size=12, color='white')
        ),
        bgcolor='rgb(20, 22, 28)' # Fundo escuro focado em dados
    ),
)
