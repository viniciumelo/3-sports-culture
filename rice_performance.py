import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Declan Rice
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Passe, Distribuição e Desarmes)', 
    'Velocidade Máxima<br>(Aceleração e Cobertura)', 
    'Chances de Gol<br>(Bolas Paradas e Infiltração)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de scouts da Premier League)
# Declan Rice pontua no topo em retenção e recuperação da posse, com boa velocidade e ótima presença em bolas paradas/infiltrações.
valores_grafico = [91, 84, 78]