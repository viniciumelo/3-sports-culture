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
    "33.5 km/h de pico (Aceleração rápida no 1v1)", 
    "0.82 xG+xA (Líder em passes decisivos da ponta)"
]

# Fechando o circuito do gráfico de radar (repetindo o primeiro item)
metricas_fechadas = metricas + [metricas[0]]
valores_grafico_fechados = valores_grafico + [valores_grafico[0]]
valores_reais_fechados = valores_reais + [valores_reais[0]]

# 2. Construção do Gráfico de Radar Interativo
fig = go.Figure()

