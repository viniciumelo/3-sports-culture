import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Mbappé
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Condução e Dribles)', 
    'Velocidade Máxima<br>(Aceleração/Sprints)', 
    'Chances de Gol<br>(Finalizações e xG)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de ligas europeias)
# Mbappé possui números extremos em velocidade e criação/finalização de chances.
valores_grafico = [88, 99, 94]  

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Alta retenção (Média de 4.8 dribles p/ jogo)", 
    "38.0 km/h de pico (Elite mundial)", 
    "0.89 xG+xA (Participação direta constante)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
