import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Yuri Alberto
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Retenção, Pivô e Movimentação)', 
    'Velocidade Máxima<br>(Arrancadas e Rupturas em Profundidade)', 
    'Chances de Gol<br>(Finalizações, Infiltrações e xG)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
# Yuri Alberto pontua muito bem em velocidade de transição ofensiva e volume de finalização.
valores_grafico = [76, 89, 85]