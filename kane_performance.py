import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Harry Kane
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Recuo, Pivô e Construção)', 
    'Velocidade Máxima<br>(Aceleração/Deslocamento)', 
    'Chances de Gol<br>(Finalizações e Assistências)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados históricos da Bundesliga/Premier League)
# Kane pontua muito alto em participação na posse e criação/conversão de chances, com nota moderada em velocidade.
valores_grafico = [86, 74, 96]  

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Excelente retenção (Média de 42 toques por jogo)", 
    "32.1 km/h de pico (Foco em posicionamento)", 
    "0.92 xG+xA (Armador e finalizador de elite)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
