import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Lionel Messi
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Dribles, Pivô e Visão)', 
    'Velocidade Máxima<br>(Aceleração Curta)', 
    'Chances de Gol<br>(Gols, Assistências e Key Passes)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados analíticos globais)
# Messi pontua no teto histórico em posse/construção e criação de chances, com nota moderada em velocidade de sprint longo.
valores_grafico = [98, 70, 97]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 65+ toques estruturando o jogo)", 
    "31.5 km/h de pico (Foco em mudança rápida de direção)", 
    "1.05 xG+xA (Líder mundial em passes que quebram linhas)"
]

