import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Cole Palmer
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Passe, Retenção e Controle)', 
    'Velocidade Máxima<br>(Aceleração e Deslocamento)', 
    'Chances de Gol<br>(Gols, Assistências e xG+xA)'
]
