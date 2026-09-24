import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Aurélien Tchouaméni
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Precisão de Passe e Retenção)', 
    'Velocidade Máxima<br>(Cobertura e Recomposição)', 
    'Chances de Gol<br>(Lançamentos e Chutes de Longe)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Tchouaméni registra notas altíssimas em passe/posse e excelente cobertura física no meio.
valores_grafico = [92, 83, 70]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Excelente retenção (Média de 90%+ de precisão nos passes e combate no meio)", 
    "33.1 km/h de pico (Grande raio de ação e recuperação defensiva)", 
    "0.28 xG+xA (Contribuição com passes verticais e finalizações de média distância)"
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
    fillcolor='rgba(65, 105, 225, 0.3)',  # Tom azul royal/França
    line=dict(color='royalblue', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Aurélien Tchouaméni'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Aurélien Tchouaméni",
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
)
