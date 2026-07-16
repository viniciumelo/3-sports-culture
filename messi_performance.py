import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Lionel Messi
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Dribles, Pivô e Visão)', 
    'Velocidade Máxima<br>(Aceleração Curta)', 
    'Chances de Gol<br>(Gols, Assistências e Key Passes)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados analíticos globais)
# Messi pontua no teto histórico em posse/construção e criação de chances, com nota moderada em velocidade de sprint longo.
valores_grafico = [98, 70, 97]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 65+ toques estruturando o jogo)", 
    "31.5 km/h de pico (Foco em mudança rápida de direção)", 
    "1.05 xG+xA (Líder mundial em passes que quebram linhas)"
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
    fillcolor='rgba(0, 128, 128, 0.3)',  # Tom azul-turquesa/celeste elegante para o layout
    line=dict(color='teal', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Lionel Messi'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Lionel Messi",
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
        bgcolor='rgb(16, 20, 26)' # Fundo escuro profissional focado em dados
    ),
    paper_bgcolor='rgb(16, 20, 26)',
    showlegend=False,
    width=700,
    height=600
)