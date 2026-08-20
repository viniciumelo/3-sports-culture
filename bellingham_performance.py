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
