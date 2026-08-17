import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Declan Rice
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Passe, Distribuição e Desarmes)', 
    'Velocidade Máxima<br>(Aceleração e Cobertura)', 
    'Chances de Gol<br>(Bolas Paradas e Infiltração)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts da Premier League)
# Declan Rice pontua no topo em retenção e recuperação da posse, com boa velocidade e ótima presença em bolas paradas/infiltrações.
valores_grafico = [91, 84, 78]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 68+ toques/jogo e 90% de acerto no passe)", 
    "33.4 km/h de pico (Intensidade em cobertura e transição)", 
    "0.45 xG+xA (Perigo em assistências, escanteios e chutes de fora da área)"
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
    fillcolor='rgba(220, 38, 38, 0.3)',  # Tom vermelho (referência ao Arsenal)
    line=dict(color='crimson', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Declan Rice'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Declan Rice",
        font=dict(size=22, color='white'),
        x=0.5,
        y=0.95
    ),
)
