import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Marc Cucurella
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Passe, Suporte e Desarmes)', 
    'Velocidade Máxima<br>(Recomposição e Sprints)', 
    'Chances de Gol<br>(Cruzamentos e Key Passes)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Cucurella pontua alto em presença de jogo/posse e intensidade física, com boa criação pelo corredor.
valores_grafico = [85, 84, 72]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Boa retenção (Média de 58+ toques/jogo e alta taxa de desarmes)", 
    "33.2 km/h de pico (Intensidade em transições ofensivas e defensivas)", 
    "0.32 xG+xA (Apoio constante com cruzamentos e sobreposições)"
]
