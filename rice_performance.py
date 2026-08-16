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

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 68+ toques/jogo e 90% de acerto no passe)", 
    "33.4 km/h de pico (Intensidade em cobertura e transição)", 
    "0.45 xG+xA (Perigo em assistências, escanteios e chutes de fora da área)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]