import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Mikel Merino
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Retenção, Duelos e Distribuição)', 
    'Velocidade Máxima<br>(Deslocamento Tático e Cobertura)', 
    'Chances de Gol<br>(Infiltrações, Cabeceios e xG+xA)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Merino pontua muito alto em duelos/posse e chegada na área, com velocidade tática sólida.
valores_grafico = [88, 77, 86]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Alta retenção (Média de 55+ toques/jogo e domínio em duelos físicos)", 
    "31.8 km/h de pico (Velocidade sustentada para transição e recomposição)", 
    "0.68 xG+xA (Excelente aproveitamento em bolas aéreas e finalizações na área)"
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
    fillcolor='rgba(220, 20, 60, 0.3)',  # Tom vermelho/carmesim (referência ao Arsenal / Espanha)
    line=dict(color='crimson', width=2),
))