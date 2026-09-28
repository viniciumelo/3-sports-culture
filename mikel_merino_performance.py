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