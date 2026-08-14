import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Joško Gvardiol
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Saída de Bola e Condução)', 
    'Velocidade Máxima<br>(Aceleração e Cobertura)', 
    'Chances de Gol<br>(Infiltração e Participação em Gols)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Gvardiol apresenta números altíssimos em posse e velocidade para um defensor, com ótimos índices de participação ofensiva.
valores_grafico = [90, 86, 75]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Alta retenção (Média de 75+ toques/jogo e construção desde a defesa)", 
    "34.1 km/h de pico (Excelente recuperação e transição)", 
    "0.35 xG+xA (Frequentes infiltrações e chute de média distância)"
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
    fillcolor='rgba(70, 130, 180, 0.3)',  # Tom azul aço (Steel Blue)
    line=dict(color='steelblue', width=2),
    text=valores_reais_fechados,
    hovertemplate="<b>%{theta}</b><br>Nível Geral: %{r}/100<br>Dado Real: %{text}<extra></extra>",
    name='Joško Gvardiol'
))

# 3. Estilização do Layout do Dashboard
fig.update_layout(
    title=dict(
        text="Análise de Desempenho Médio - Joško Gvardiol",
        font=dict(size=22, color='white'),
        x=0.5,
        y=0.95
    ),
)
