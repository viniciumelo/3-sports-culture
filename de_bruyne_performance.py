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

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Retenção de elite (Média de 70+ toques/jogo organizando o meio)", 
    "33.0 km/h de pico (Condução potente em transição)", 
    "0.96 xA+xG (Líder em passes decisivos que quebram linhas)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]