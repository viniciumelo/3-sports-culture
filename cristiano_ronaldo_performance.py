import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Cristiano Ronaldo
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Toques na Área/Retenção)', 
    'Velocidade Máxima<br>(Aceleração/Sprints)', 
    'Chances de Gol<br>(Gols Esperados - xG e Volume)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada no perfil analítico do jogador)
# CR7 pontua no topo histórico em finalização e volume de chances, mantendo boa velocidade e menor retenção de bola.
valores_grafico = [68, 88, 97]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Foco em definição (Poucos toques, alta eficiência)", 
    "34.2 km/h de pico (Sprints verticais)", 
    "0.95 xG (Volume extremo de finalizações)"
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
    fillcolor='rgba(255, 69, 0, 0.3)',  # Tom vermelho/laranja vibrante
    line=dict(color='orangered', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Cristiano Ronaldo'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Cristiano Ronaldo",
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
        bgcolor='rgb(17, 17, 17)' # Fundo escuro estilo premium analytics
    ),
)