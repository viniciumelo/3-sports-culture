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