import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Arda Güler
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Dribles, Controle e Passe)', 
    'Velocidade Máxima<br>(Agilidade e Aceleração)', 
    'Chances de Gol<br>(Key Passes, Finalização e xG+xA)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Arda Güler registra números de destaque em criação de chances e controle técnico sob pressão.
valores_grafico = [89, 81, 91]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Alta retenção (Média de 48+ toques/jogo e visão sob pressão)", 
    "32.9 km/h de pico (Aceleração rápida e mudança de direção)", 
    "0.82 xG+xA (Eficiência alta em passes decisivos e chutes da entrada da área)"
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
    fillcolor='rgba(255, 215, 0, 0.3)',  # Tom dourado (referência ao Real Madrid)
    line=dict(color='gold', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Arda Güler'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Arda Güler",
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
        bgcolor='rgb(18, 20, 26)' # Fundo escuro estilo dashboard profissional
    ),
)
