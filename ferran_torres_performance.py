import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Ferran Torres
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os valores reais de scouts profissionais aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Associação e Movimentação)', 
    'Velocidade Máxima<br>(Aceleração e Sprints)', 
    'Chances de Gol<br>(Gols Esperados - xG e Finalizações)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados de desempenho)
# Ferran Torres apresenta um perfil bastante equilibrado entre infiltração, velocidade e apoio à posse.
valores_grafico = [78, 85, 82]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Boa retenção (Média de 35 toques/jogo e apoios)", 
    "33.8 km/h de pico (Ataque aos espaços)", 
    "0.62 xG+xA (Volume constante de chances na área)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]