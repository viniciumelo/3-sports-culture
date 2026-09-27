import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Mateo Kovačić
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Condução Progressiva e Retenção)', 
    'Velocidade Máxima<br>(Agilidade e Transição em Condução)', 
    'Chances de Gol<br>(Passes Decisivos e Construção)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Kovačić pontua extremamente alto em retenção e condução de posse sob pressão.
valores_grafico = [93, 84, 68]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Maestria na retenção (Média de 90%+ de acerto no passe e alta progressão com bola)", 
    "32.8 km/h de pico (Velocidade dinâmica de transição e quebra de linhas)", 
    "0.35 xG+xA (Participação na criação e pré-assistências no último terço)"
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
    fillcolor='rgba(0, 102, 204, 0.3)',  # Tom azul (referência à Croácia / Manchester City)
    line=dict(color='dodgerblue', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Mateo Kovačić'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Mateo Kovačić",
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
        bgcolor='rgb(16, 20, 28)' # Fundo escuro estilo dashboard profissional
    ),
    paper_bgcolor='rgb(16, 20, 28)',
    showlegend=False,
    width=700,
    height=600
)
