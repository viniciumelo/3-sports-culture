import plotly.graph_objects as go

# 1. Definição das métricas e os valores médios de desempenho do Rúben Dias
# Os valores do gráfico estão em escala de 0 a 100 para manter a proporção visual ideal,
# enquanto os dados de scout especializado aparecem no detalhamento (hover).
metricas = [
    'Posse de Bola<br>(Saída de Bola e Volume de Passe)', 
    'Velocidade Máxima<br>(Recuperação e Cobertura)', 
    'Chances de Gol<br>(Cabeceio e Passes Progressivos)'
]

# Notas visuais de desempenho (Escala de 0 a 100 baseada em dados analíticos da Premier League)
valores_grafico = [93, 83, 62]

# Dados reais detalhados que aparecem ao passar o mouse (hover)
valores_reais = [
    "Construção de elite (Média de 85+ toques/jogo e 93% de acerto de passe)", 
    "33.1 km/h de pico (Excelente timing de desarme e recuperação)", 
    "0.18 xG+xA (Presença em escanteios e lançamento longo)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]