import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Michael Olise
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Dribles e Retenção)', 
    'Velocidade Máxima<br>(Aceleração e Sprints)', 
    'Chances de Gol<br>(Key Passes, Bolas Paradas e xA)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Olise registra números altíssimos em criação de chances e drible curto.
valores_grafico = [88, 85, 93]