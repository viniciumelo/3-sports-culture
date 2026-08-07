import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Kevin De Bruyne
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Retenção e Distribuição)', 
    'Velocidade Máxima<br>(Aceleração e Condução)', 
    'Chances de Gol<br>(Key Passes e Assistências Esperadas)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada no perfil analítico do jogador)
# De Bruyne pontua no teto global em criação de chances e controle de posse de bola.
valores_grafico = [94, 82, 98]