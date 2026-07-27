import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Lamine Yamal
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Dribles e Retenção)', 
    'Velocidade Máxima<br>(Aceleração e Sprints)', 
    'Chances de Gol<br>(Criação de Chances e xG)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts)
valores_grafico = [92, 86, 90]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Alta retenção (Média de 5.2 dribles tentados/jogo)", 
]

