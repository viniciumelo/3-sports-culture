import plotly.graph_objects as go

# 1. Definição das métricas que você pediu e os valores fictícios médios do Kvara
# Para o visual ficar perfeito, os valores do gráfico estão normalizados (0 a 100)
# Mas os valores reais são exibidos ao passar o mouse.
metricas = [
    'Posse de Bola<br>(Retenção sob Pressão)', 
    'Velocidade Máxima<br>(Aceleração/Sprint)', 
    'Chances de Gol<br>(Gols + Assistências Esperadas)'
]

# Notas visuais de desempenho (Escala 0 a 100 baseada em scouts europeus)
valores_grafico = [85, 92, 88]  

# Dados reais detalhados para aparecerem na legenda interativa (hover)
valores_reais = [
    "85% de eficiência", 
    "34.8 km/h de pico", 
    "0.75 xG+xA por jogo"
]
